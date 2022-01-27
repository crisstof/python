"""Simpletest Example that shows how to get temperature,
   pressure, and altitude readings from a BMP280"""
import time
import board
import busio
import digitalio # For use with SPI
import adafruit_bmp280

#spi = board.SPI()
spi = board.SPI()
bmp_cs = digitalio.DigitalInOut(board.CE1)
bmp280 = adafruit_bmp280.Adafruit_BMP280_SPI(spi,bmp_cs)


# change this to match the location's pressure (hPa) at sea level
bmp280.sea_level_pressure = 1013.25

class Sensor:
    def __init__(self, parent=None):
        super().__init__(parent)
        
    def get_Temperature(self):
        while True:
            return bmp280.temperature
            time.sleep(3)
    def get_Pressure(self):
        while True:
            return bmp280.pressure
            time.sleep(3)
    def get_Altitude(self):
        while True:
            return bmp280.altitude
            time.sleep(3)
    
        
        
    

