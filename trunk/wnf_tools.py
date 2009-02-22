#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#import sys
import os
import tempfile
import time
import datetime
import calendar

clBlack = (0,0,0)
clWhite = (255,255,255)
clRed = (255,0,0)
clGreen = (0,255,0)
clBlue = (0,0,255)
clGray = (100,100,100)
clYellow = (255,255,0)
clTuerkis = (0,255,255)
clLime = (0,255,0)

cFontVerdana = "/usr/share/fonts/truetype/msttcorefonts/verdana.ttf"
cFontArial = "/usr/share/fonts/truetype/msttcorefonts/Arial.ttf"
cFontTimes = "/usr/share/fonts/truetype/msttcorefonts/times.ttf"
cFontDejaVuSans = "/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans.ttf"

cWochentageL = ("Montag","Dienstag","Mittwoch","Donnerstag","Freitag","Samstag","Sonntag")


def forceDir(aPfad):
    if not os.path.exists(aPfad):
        os.makedirs(aPfad)
    return os.path.exists(aPfad)

def tempDateiname(aExtension):
    #http://docs.python.org/lib/module-tempfile.html
    #die Datei muss vom Anwender gelöscht werden
    f,s = tempfile.mkstemp(aExtension,"wnf_")
    #da die Datei geöffnet zurückgegeben wird , schließe ich sie jetzt
    os.close(f)
    return s

def dateiStarten(aDateiname):
    if aDateiname.endswith(".bmp"):
        s = "gwenview %s" % aDateiname
    elif aDateiname.endswith(".jpg"):
        s = "gwenview %s" % aDateiname
    elif aDateiname.endswith(".png"):
        s = "gwenview %s" % aDateiname
    else:
        s = aDateiname
    os.system(s)

def pascalToRGB(s,aDefault):
    if s=="clYellow":
        return clYellow
    elif s=="clLime":
        return clLime
    elif s=="clBlack":
        return clBlack
    elif s=="clWhite":
        return clWhite
    elif s=="clRed":
        return clRed
    elif s=="clBlue":
        return clBlue
    elif s=="clGreen":
        return clGreen
    elif s.startswith("$00"):
        b=int(s[3:5],16)
        g=int(s[5:7],16)
        r=int(s[7:9],16)
        return (r,g,b)
    else:
        return aDefault

def rgbToHTML(RGB):
    s="#%s%s%s" % (hex(RGB[0])[-2:],hex(RGB[1])[-2:],hex(RGB[2])[-2:])
    return s

def paramStr(args,ipos):
    s=""
    i=0
    for a in args:
        if i==ipos:
           s=a
           break
        i=i+1
    return s

def zeitraum_ueberlappt(d1von,d1bis,d2von,d2bis):
    #zeitraum 1 liegt vor zeitraum 2
    if (d1bis<d2von):
        b=False
    #zeitraum 1 liegt nach zeitraum 2
    elif (d1von>d2bis):
        b=False
    else:
        b=True
    return b

def isSchaltjahrJJ(jj):
    if (jj%400) == 0:
         return True
    elif (jj%100) == 0:
         return False
    elif (jj%4) == 0:
         return True
    return False

def isSchaltjahr(d):
    jj = d.year
    return isSchaltjahr(jj)

def strToDate(s):
    return datetime.date(*time.strptime(s, "%d.%m.%Y")[0:3])

def dateToStr(d):
    return d.strftime("%d.%m.%Y")

def strToInt(s):
    try:
        return int(s)
    except:
        return 0

def alterInJahren(aVon,aBis):
    jv = aVon.year
    jb = aBis.year
    return jb - jv

def diesesJahr(d,aDiesesJahr):
    jj = aDiesesJahr.year
    mm = d.month
    tt = d.day
    if (mm==2) and (tt>28):
        if not isSchaltjahrJJ(jj):
            tt=28
    return datetime.date(jj,mm,tt)

def ersterDieserWoche(d):
    w = calendar.weekday(d.year,d.month,d.day)
    d = d + datetime.timedelta(days=-w)
    # print w, d
    return d

def wochentag_i(d):
    w = calendar.weekday(d.year,d.month,d.day)
    return w

#Datum des Ostersonntags
def ostersonntag(jahr):
    a = jahr%19
    b,c = divmod(jahr,100)
    d,e = divmod(b,4)
    f = (b+8)/25
    g = (b-f+1)/3
    h = (19*a+b-d-g+15)%30
    i,k = divmod(c,4)
    l = (32+2*e+2*i-h-k)%7
    m = (a+11*h+22*l)/451
    mon,tag = divmod(h+l-7*m+114,31)
    return (jahr,mon,tag+1)

#Tagesnummer des Datums
def tagesnummer(jj,mm,tt):
    tn=0
    if mm>1:
        tn=tn+31
    if mm>2:
        tn=tn+28
    if mm>3:
        tn=tn+31
    if mm>4:
        tn=tn+30
    if mm>5:
        tn=tn+31
    if mm>6:
        tn=tn+30
    if mm>7:
        tn=tn+31
    if mm>8:
        tn=tn+31
    if mm>9:
        tn=tn+30
    if mm>10:
        tn=tn+31
    if mm>11:
        tn=tn+30
    tn=tn+tt
    if isSchaltjahrJJ(jj) and (mm>2):
        tn=tn+1
    return tn

#Tagesnummer des Ostersonntags
def ostersonntag_tn(jahr):
    jj,mm,tt = ostersonntag(jahr)
    tn = tagesnummer(jj,mm,tt)
    return (tn)

cSN = 'SN'
cBY = 'BY'
cSH = 'SH'
cBE = 'BE'
cMV = 'MV'
cBB = 'BB'
cST = 'ST'
cTH = 'TH'
cHH = 'HH'
cHB = 'HB'
cNW = 'NW'
cHS = 'HS'
cBW = 'BW'
cRP = 'RP'
cSL = 'SL'


def sFeiertag(d,aBundesland):
    jj=d.year
    mm=d.month
    tt=d.day
    os = ostersonntag_tn(jj)
    tn = tagesnummer(jj,mm,tt)
    s=""
    if tn == os:
        s= "Ostersonntag"
    elif tn==os+1:
        s="Ostermontag"
    elif tn==os-2:
        s = "Karfreitag"
    elif tn == os + 39:
        s= 'Himmelfahrt'
    elif tn == os + 49:
        s = "Pfingstsonntag";
    elif tn == os + 50:
        s = "Pfingstmontag"
    elif (tn == os + 60) and (aBundesland in [cBW, cBY, cHS, cNW, cRP, cSL]):
        s = "Fronleichnam"
    elif (mm==01) and (tt==01):
        s = "Neujahr"
    elif (mm==05) and (tt==01):
        s = "Maifeiertag"
    elif (mm==10) and (tt==03):
        s = "Tag der Einheit"
    elif (mm==12) and (tt==25):
        s = "Weihnachten"
    elif (mm==12) and (tt==26):
        s = "Weihnachten"
    elif (mm==01) and (tt==06) and (aBundesland in [cBW, cBY, cST]):
        s = "Heilige Drei Könige"
    elif (mm==8) and (tt==15) and (aBundesland in [cBY, cSL]):
        s = "Mariä Aufnahme"
    elif (mm==10) and (tt==31) and (aBundesland in [cBB, cMV, cSN, cST, cTH]):
        s = "Reformationstag"
    elif (mm==11) and (tt==01) and (aBundesland in [cBW, cBY, cNW, cRP, cSL]):
        s = "Allerheiligen"
    return(s)

def alleFeiertage(jj,aBundesland):
    d=datetime.date(jj,01,01)
    difference1 = datetime.timedelta(days=1)
    for i in range(365):
        s=sFeiertag(d,aBundesland)
        if s<>"":
            print d,s
        d=d+difference1

if __name__ == "__main__":
    print "Ostersonntag ",ostersonntag_tn(2008)
    alleFeiertage(2008,cSN)
    cl=pascalToRGB("$0080FFFF",clWhite)
    print cl
    print zeitraum_ueberlappt((2008,01,01),(2008,12,31),(2008,03,01),(2008,03,31))
