import machine
from machine import I2C, ADC, Pin, SoftI2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
import utime as time
from time import sleep
import rp2
from dht import DHT11


class WaterLevel:
    def __init__(self, level_min, level_max, ADC_Pin):
        self.level_min = level_min
        self.level_max = level_max
        self.ADC_Pin = ADC_Pin
        
    def percentage(self):            
        self.level_cur = ADC(Pin(self.ADC_Pin))
        self.level_range = self.level_max - self.level_min
        
        self.corrected_min = self.level_cur.read_u16() - self.level_min
        self.percentage = (self.corrected_min * 100) / self.level_range
        if self.percentage <= 0:
            self.percentage = 0
            return self.percentage
        elif self.percentage >=100:
            self.percentage = 100
            return self.percentage
        else:
            int(self.percentage)
            return self.percentage



## Object setups
# Setup DHT Sensor
dhtPIN = 16
dhtSensor = DHT11(Pin(dhtPIN, Pin.OUT, Pin.PULL_DOWN))   

# Setup LCD 
i2c = I2C(0, sda=Pin(0),scl=Pin(1), freq=100000)
print(i2c.scan())
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)


## Main Loop (TEST)
while True:
    Tank1 = WaterLevel(39000,65535,26)
    sleep(1)
    dhtSensor.measure()
    lcd.clear()
    lcd.putstr("Water Lvl 1:"+ str(Tank1.percentage())+"%\n")
    sleep(2)
    lcd.clear()
    lcd.putstr("Temp:"+ str(dhtSensor.temperature())+" C\n" \
           "Hum : " + str(dhtSensor.humidity())+"%\n")
    sleep(1)

        
        