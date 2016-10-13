#coding:utf-8
import pytesser
from pytesser import *
import ImageEnhance

image = Image.open('.\\getJPEG.gif')

#使用ImageEnhance可以增强图片的识别率
enhancer = ImageEnhance.Contrast(image)
image_enhancer = enhancer.enhance(4)

print image_to_string(image_enhancer)