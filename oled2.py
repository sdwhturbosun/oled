#sudo pip3 install luma.oled
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106
import ds3231
import time
import RPi.GPIO as gpio
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(13,gpio.OUT)
gpio.output(13,0)
def shi2bcd(shi):
    shiwei=int(shi/10)    
    gewei=shi%10
    bcd=(shiwei<<4)+gewei
    return bcd
isweek=input("please alarm type(day|date):")
if isweek=="day":
    dateorday=int(input("please input day(1-7)"))
    ds=ds3231.DS3231(0x68,True)
else:
    dateorday=int(input("please input date(1-31)"))
    ds=ds3231.DS3231(0x68,False)
t=ds.gettime()
print(t)
amorpm=input("please input AM or PM(12 hours):")
m1=int(input("please input minute for alarm1:"))
h1=int(input("please input hour for alarm1:"))
ds.setalarm1(0,m1,h1,dateorday,amorpm)
ds.clearalarm1status()

while True:
    am1status=ds.getalarm1status()
    if am1status:
        gpio.output(13,1)
    else:
        gpio.output(13,0)
    t=ds.gettime()
    d=ds.getdate()
    weekday=ds.getweekday()
    serial=i2c(port=1,address=0x3c)
    device=sh1106(serial)
    with canvas(device) as screen:
        #screen.rectangle(device.bounding_box,outline="white",fill="black")   
        screen.text((0,10),"now:"+t,fill="white")
        screen.text((0,20),d+" "+weekday,fill="white")
        screen.text((0,30),"alarm time:"+str(h1)+":"+str(m1)+":00"+amorpm,fill="white")
        
    time.sleep(1)
    
