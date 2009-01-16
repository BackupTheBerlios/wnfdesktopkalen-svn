#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class TwnfSVG:
    def __init__(self,aDateiname):
        self.dateiname = aDateiname
        self.font_n = "dejavusans"
        self.font_n_size = 10

    def open(self,aCaption,w,h):
        self.fd=open(self.dateiname,"w")
        s='<svg xmlns="http://www.w3.org/2000/svg" width="%i" height="%i"' % (w,h)
        self.fd.write(s)
        s='  xmlns:xlink="http://www.w3.org/1999/xlink">'
        self.fd.write(s)
        self.fd.write("\n")
        s='<title> %s</title>' % (aCaption)
        self.fd.write(s)
        self.fd.write("\n")

    def write(self,s):
        self.fd.write(s)
        self.fd.write("\n")

    def close(self):
        s='</svg>'
        self.write(s)
        self.fd.close

    def desc(self,aDescription):
        s='<desc>%s</desc>' % (aDescription)
        self.write(s)

    def kommentar(self,aKommentar):
        s='<!-- %s -->' % (aKommentar)
        self.write(s)

    def text_anchor(self,x,y,text,aAnchor,aFont,aSize,aWeight):
        s='<text x="%i" y="%i" text-anchor="%s" style="font-family:%s; font-size:%ipx; font-weight:%s;">' % \
            (x,y,aAnchor,aFont,aSize,aWeight)
        self.write(s)
        s=text
        self.write(s)
        s='</text>'
        self.write(s)

    def text(self,x,y,text,aFont,aSize,aWeight):
	#linksbündig
        self.text_anchor(x,y,text,"begin",self.font_n,self.font_n_size,"")

    def text_center(self,x,y,text,aFont,aSize,aWeight):
	#zentriert
        self.text_anchor(x,y,text,"middle",self.font_n,self.font_n_size,"")

    def text_right(self,x,y,text,aFont,aSize,aWeight):
	#rechtsbündig
        self.text_anchor(x,y,text,"end",self.font_n,self.font_n_size,"")

    def text_n(self,x,y,text):
	#normal, linksbündig
        self.text(x,y,text,self.font_n,self.font_n_size,"")

    def text_nc(self,x,y,text):
	#normal zentriert
        self.text_center(x,y,text,self.font_n,self.font_n_size,"")

    def text_b(self,x,y,text):
	#bold linksbündig
        self.text(x,y,text,self.font_n,self.font_n_size,"bold")

    def rect_komplett(self,x,y,w,h,stroke_color,stroke_width,fill_color,fill_opacity):
        s="""
            <rect x="%i" y="%i" width="%i" height="%i"
              stroke-width="%ipx" stroke="%s" fill="%s"  fill-opacity="%f" />
          """ % (x,y,w,h,stroke_width,stroke_color,fill_color,fill_opacity)
        self.write(s)

    def rect(self,x,y,w,h,fill_color):
	self.rect_komplett(x,y,w,h,fill_color,1,fill_color,0.7)
