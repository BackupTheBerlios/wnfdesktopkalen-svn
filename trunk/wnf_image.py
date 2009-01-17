#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import wnf_tools

class TwnfImage:
    def __init__(self,aBreite,aHoehe,aFontname,aFontsize,aHGColor,aTextColor,aLineColor):
        self.Breite = aBreite
        self.Hoehe = aHoehe
        self.im = Image.new('RGB', (aBreite,aHoehe))
        self.draw =  ImageDraw.Draw(self.im)
        self.font_n_size = aFontsize
        if aFontname<>"":
            self.font_n = ImageFont.truetype(aFontname,self.font_n_size)
        else:
            self.font_n = ImageFont.load_default()
        self.TextColor = aTextColor
        self.LineColor = aLineColor
        #weißen Hintergrund einstellen
        self.draw.rectangle((0,0,aBreite,aHoehe),fill=aHGColor)
        tw,self.TextHeight = self.font_n.getsize("Hg");

    def line(self,x1,y1,x2,y2):
        self.draw.line((x1,y1,x2,y2),fill=self.LineColor)

    def rect(self,x,y,b,h):
        self.line(x,y,x+b,y)
        self.line(x+b,y,x+b,y+h)
        self.line(x+b,y+h,x,y+h)
        self.line(x,y+h,x,y)

    def rectcl(self,x,y,b,h,cl):
        self.draw.rectangle((x,y,x+b,y+h),fill=cl)

    def rectclrand(self,x,y,b,h,cl):
        self.draw.rectangle((x,y,x+b,y+h),outline=self.LineColor,fill=cl)

    def show(self):
        dn = wnf_tools.TempDateiname(".bmp")
        self.save(dn)
        wnf_tools.DateiStarten(dn)
        os.remove(dn)

    def text(self,x,y,text,aFont,aSize,aWeight):
        if aFont=="":
            self.draw.text((x,y),text,fill=self.TextColor)
        else:
            self.draw.text((x,y),text,font=aFont,fill=self.TextColor)

    def text_cl(self,x,y,text,aFontname,aSize,cl):
        f = ImageFont.truetype(aFontname,aSize)
        if f=="":
            self.draw.text((x,y),text,fill=cl)
        else:
            self.draw.text((x,y),text,font=f,fill=cl)

    def text_n(self,x,y,text):
        self.text(x,y,text,self.font_n,self.font_n_size,"")

    def text_b(self,x,y,text):
        self.text(x,y,text,self.font_n,self.font_n_size,"bold")

    def text_box(self,x,y,b,h,text,cl):
        self.rectcl(x,y,b,h,cl)
        tw,th = self.font_n.getsize(text);
        #falls der Text nicht in die Textbox passt den string kürzen
        while tw>b-4:
            text=text[:len(text)-1]
            tw,th = self.font_n.getsize(text);
        self.text_n(x+2,y,text)

    def text_box_c(self,x,y,b,h,text,cl,halign="center"):
        from math import floor
        self.rectcl(x,y,b,h,cl)
        tw,th = self.font_n.getsize(text);
        #falls der Text nicht in die Textbox passt den string kürzen
        while tw>b-4:
            text=text[:len(text)-1]
            tw,th = self.font_n.getsize(text);
        if halign == "center":
            leftStart = x + ((b - tw) / 2)
        elif halign == "right":
            leftStart = x+b-tw
        else:
            leftStart = x

        self.text_n(leftStart,y,text)

    def hintergrundbild(self,x,y,dn):
        try:
            hg = Image.open(dn)
            (b,h) = hg.size
            self.im.paste(hg,(x,y,b,h))
        except:
            print dn, ' existiert nicht.'
            
    def save(self,dn):
        self.im.save(dn)

    def text_countdown(self,x,y,b,h,text,aFontname,aFontSize,cl):
        #zeichnet den Text unten zentriert mit dem Font und in der Farbe
        f = ImageFont.truetype(aFontname,aFontSize)
        if f<>"":
            tw,th = f.getsize(text);
            y = y + h - th
            x = x + ((b - tw) / 2)
            self.draw.text((x,y),text,font=f,fill=cl)

if __name__ == "__main__":
    im = TwnfImage(600,400,wnf_tools.cFontTimes,10,wnf_tools.clWhite,wnf_tools.clBlack,wnf_tools.clBlack)
    #im.rect(10,10,80,80)
    #im.rectcl(10,10,80,10,wnf_tools.clRed)
    s="Hg Ostersonntag Hg"
    th = im.TextHeight;
    for i in range(4):
        im.rect(10,10+(th*i),80,th)
        im.text_box_c(10,10+(th*i),80,th,s,wnf_tools.clRed)
##        im.text_box(10,10+(th*i),80,th,s,wnf_tools.clRed)
    im.rect(100,100,80,60)
    im.text_countdown(100,100,80,60,"50",wnf_tools.cFontArial,24,wnf_tools.clLime)
    im.show()
