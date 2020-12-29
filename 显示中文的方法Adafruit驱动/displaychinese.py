#安装python驱动模块  sudo pip3 install Adafruit-SSD1306
import time
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
RST=24
disp=Adafruit_SSD1306.SSD1306_128_32(rst=RST)#取得显示器对象
disp.begin()
width=disp.width#取显示器宽度
height=disp.height#取显示器高度
image=Image.new('1',(width,height))#创建图像对象
draw=ImageDraw.Draw(image)#创建image图像缓存画布，先在缓存这里画好，再推送到display显示。
#显示英文，创建系统默认字体
#font=ImageFont.load_default()
#定义字体，这里显示中文只支持ttf字体，放到程序目录中即可
font=ImageFont.truetype('heiti.ttf',15)
padding=0
top=padding
bottom=height-padding
x=0  #定义内容放置的横坐标
draw.text((x,top),u'心率:100',font=font,fill=255)  #加u表示使用unicode编码汉字
disp.image(image)
disp.display()
time.sleep(1)
#下面演示如何不闪屏显示动态内容
for i in range(1000):
    #通过画一个满屏的黑色矩形来清除图像缓存
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    #在图像缓存画布上画好内容
    draw.text((x,top),str(i),font=font,fill=255)
    
    disp.image(image)#将图像推送到disp
    
    disp.display()#显示