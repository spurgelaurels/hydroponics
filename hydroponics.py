import machine
from machine import I2C, ADC, Pin, SoftI2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
import time
from time import sleep
import rp2

adc_waterlevel1 = ADC(Pin(26))
waterlevel1_min = 30000
waterlevel1_max = 36488

adc_waterlevel2 = ADC(Pin(27))
adc_waterlevel3 = ADC(Pin(28))


i2c = I2C(0, sda=Pin(0),scl=Pin(1), freq=100000)
print(i2c.scan())
I2C_ADDR = i2c.scan()[0]

lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

while True:
    
#     lcd.clear()
#     lcd.putstr("level: "+ str(adc_waterlevel1.read_u16())+"\n")
#     sleep(2)



    lcd.clear()
    range = waterlevel1_max - waterlevel1_min
#     lcd.putstr("range:\n"+ str(range))
#     sleep(2)
    
    lcd.clear()
    correctedStartValue = adc_waterlevel1.read_u16() - waterlevel1_min
    lcd.putstr("level: "+ str(adc_waterlevel1.read_u16())+"\n")
#     lcd.putstr("start: "+ str(correctedStartValue)+"\n")
    sleep(2)
    
    lcd.clear()
    percentage = (correctedStartValue * 100) / range
    if percentage <= 0:
        percentage = 0
    else:
        int(percentage)
    
    lcd.putstr("W Lvl 1:"+ str(percentage)+"%\n")
    sleep(1)
  
  
  
  
  
  
#     print(I2C_ADDR)
#     lcd.blink_cursor_on()
#     lcd.putstr("I2C Address:"+str(I2C_ADDR)+"\n")
#     lcd.putstr("Tom's Hardware")
#     sleep(2)
#     lcd.putstr("Tom's Hardware")
#     sleep(2)
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
        
        