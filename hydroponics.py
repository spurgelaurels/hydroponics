import machine
from machine import I2C, ADC, Pin, SoftI2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
import time
from time import sleep
import rp2

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


i2c = I2C(0, sda=Pin(0),scl=Pin(1), freq=100000)
print(i2c.scan())
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

while True:
    Tank1 = WaterLevel(39000,65535,26)
    lcd.clear()
    lcd.putstr("W Lvl 1:"+ str(Tank1.percentage())+"%\n")
    sleep(1)


  
  
  
  
  
  
  
  
  
  # adc_waterlevel1 = ADC(Pin(26))
# waterlevel1_min = 30000
# waterlevel1_max = 36488
# 
# adc_waterlevel2 = ADC(Pin(27))
# adc_waterlevel3 = ADC(Pin(28))
  
  
  
#     print(I2C_ADDR)
#     lcd.blink_cursor_on()
#     lcd.blink_cursor_off()
#     lcd.clear()
#     lcd.putstr("Backlight Test")
#     for i in range(10):
#         lcd.backlight_on()
#         sleep(0.2)
#         lcd.backlight_off()
#         sleep(0.2)
#     lcd.backlight_on()
#     lcd.hide_cursor()
#     for i in range(20):
#         lcd.putstr(str(i))
#         sleep(0.4)
#         lcd.clear()
        
        