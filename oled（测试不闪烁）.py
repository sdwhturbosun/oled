#sudo pip3 install luma.oled
from luma.core.interface.serial import i2c,spi
from luma.core.render import canvas
from luma.oled.device import sh1106
import time
serial1=i2c(port=1,address=0x3C)
device=sh1106(serial1)
i=0
'''
while i<100:
    with canvas(device) as draw:
        draw.rectangle(device.bounding_box,outline="white",fill=0)
        draw.text((40,30),time.strftime('%H:%M:%S',time.localtime(time.time())),fill=255)
    time.sleep(0.3)
    i=i+1
'''
while True:
    with canvas(device) as draw:   
        draw.text((20,20),"time ok"+str(i),fill=100)
    i+=1
        