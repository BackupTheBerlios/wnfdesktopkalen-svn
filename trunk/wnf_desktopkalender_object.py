#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
import time

import ConfigParser
import datetime
import os
import wnf_image
import wnf_svg
import wnf_tools

class TwnfDesktopKalender:

    def __init__(self):
        self.heute = datetime.date.today()
        self.jetzt = datetime.datetime.now()
        self.wochentag_i = wnf_tools.Wochentag_i(self.heute)
        self.von = wnf_tools.ErsterDieserWoche(self.heute)
        self.bis = self.von + datetime.timedelta(days=28)
        #print self.von,self.bis
        self.termine = {}
        self.caption = "wnfDesktopKalender 0.5"
        self.Breite = 800
        self.Hoehe = 600
        self.TagBreite = 90
        self.TagHoehe = 70
        self.TagRand = 2
        self.IniDateiname = ''
        self.XOffset = 20
        self.YOffset = 20
        self.HGColor = wnf_tools.clWhite;
        self.TextColor = wnf_tools.clBlack;
        self.LineColor = wnf_tools.clBlack;
        self.FarbeFT = wnf_tools.clGray;
        self.FarbeHeute = wnf_tools.clGray;
        self.FarbeTransparent = wnf_tools.clWhite;
        self.FarbeSA = wnf_tools.clGray;
        self.FarbeSO = wnf_tools.clGray;
        self.FarbeNormal = wnf_tools.clWhite;
        self.GrafikD = ""
        self.TextFont = wnf_tools.cFontDejaVuSans
        self.TextFontSize = 9
        self.Bundesland = wnf_tools.cSN
        self.CountDown = wnf_tools.StrToDate('03.04.2008')
        self.CountDownFont = ""
        self.CountDownFontSize = 18
        self.FarbeCountDown = wnf_tools.clWhite;

    def eintragen(self, d, n, c):
        t = self.termine.get(d)
        if t == None:
            t = {}
        t[n] = c
        self.termine[d] = t

    def get_termin(self, d, i):
        s = ""
        cl = (0, 0, 0)
        t = self.termine.get(d)
        if t <> None:
            j = 0;
            for n, c in t.items():
                if j == i:
                    s = n
                    cl = c
                    break
                j = j + 1
        return s, cl

    def ausgabe(self):
        print len(self.termine)
        for d, t in self.termine.items():
            for n, c in t.items():
                print "Datum :", wnf_tools.DateToStr(d), n

    def ausgabe_28(self):
        b = 16
        d = self.von
        difference1 = datetime.timedelta(days=1)
        print "=" * (7 * b + 1)
        print self.caption
        print "=" * (7 * b + 1)
        s = "|%15s|%15s|%15s|%15s|%15s|%15s|%15s|" % wnf_tools.cWochentageL
        print s
        for w in range(4):
            sd = "|"
            s0 = "|"
            s1 = "|"
            s2 = "|"
            s3 = "|"
            s4 = "|"
            for t in range(7):
                sd = "%s%15s|" % (sd, wnf_tools.DateToStr(d))
                s, cl = self.get_termin(d, 0)
                s0 = "%s%15s|" % (s0, s[:14])
                s, cl = self.get_termin(d, 1)
                s1 = "%s%15s|" % (s1, s[:14])
                s, cl = self.get_termin(d, 2)
                s2 = "%s%15s|" % (s2, s[:14])
                s, cl = self.get_termin(d, 3)
                s3 = "%s%15s|" % (s3, s[:14])
                s, cl = self.get_termin(d, 4)
                s4 = "%s%15s|" % (s4, s[:14])
                d = d + difference1
            print "=" * (7 * b + 1)
            print sd
            print "-" * (7 * b + 1)
            print s0
            print s1
            print s2
            print s3
            print s4
        print "=" * (7 * b + 1)

    def ausgabe_svg(self, dn):
        d = self.von
        difference1 = datetime.timedelta(days=1)
        fd = wnf_svg.TwnfSVG(dn)
        tr = self.TagRand + 2
        w = tr + (self.TagBreite + tr) * 7;
        h = tr + tr + tr + (self.TagHoehe + tr) * 4 + (self.TextFontSize + 2) * 1;
        fd.open(self.caption, w + 4, h + 4)
        fd.desc("erstellt aus : %s" % (self.IniDateiname))
        fd.kommentar(self.caption)
        #rahmen um alles
        #fd.rect(0,0,w,h)
        x = tr
        y = tr
        #xc wird für die zentrierte Ausgabe benoetigt
        xc = self.TagBreite / 2
        th = self.TextFontSize + 2
        farbe = wnf_tools.RGBToHTML(self.FarbeNormal)
        for c in range(7):
            fd.rect(x, y, self.TagBreite, th + 4, farbe)
            s = wnf_tools.cWochentageL[c]
            fd.text_nc(x + xc, y + th, s)
            x = x + self.TagBreite + tr
        y = y + th + tr + tr
        for z in range(4):
            x = tr
            for c in range(7):
                if (d == self.heute) and (self.FarbeHeute <> self.FarbeTransparent):
                    cl = self.FarbeHeute
                elif (wnf_tools.sFeiertag(d, self.Bundesland) <> "") and (self.FarbeFT <> self.FarbeTransparent):
                    cl = self.FarbeFT
                elif (w == 7) and (self.FarbeSO <> self.FarbeTransparent):
                    cl = self.FarbeSO
                elif (w == 6) and (self.FarbeSA <> self.FarbeTransparent):
                    cl = self.FarbeSA
                elif (self.FarbeNormal <> self.FarbeTransparent):
                    cl = self.FarbeNormal
                else:
                    cl = self.FarbeTransparent
                if cl == self.FarbeTransparent:
                    farbe = ''
                else:
                    farbe = wnf_tools.RGBToHTML(cl)
                fd.rect(x, y, self.TagBreite, self.TagHoehe, farbe)
                s = wnf_tools.DateToStr(d)
                fd.text_nc(x + xc, y + th, s)
                for i in range(4):
                    s, cl = self.get_termin(d, i)
            if s <> '':
                if cl == self.FarbeTransparent:
                    farbe = ''
                else:
                    farbe = wnf_tools.RGBToHTML(cl)
                    fd.rect(x, y + 2 + (th * (i + 1)), self.TagBreite, th, farbe)
                fd.text_nc(x + xc, y + (th * (i + 2)), s)
                d = d + difference1
                x = x + self.TagBreite + tr
            y = y + self.TagHoehe + tr;
        fd.close()

    def ausgabe_html(self, aMitKopf):
        d = self.von
        difference1 = datetime.timedelta(days=1)
        t = ""
        if aMitKopf:
            t = "<html><body>\n"
        html = '%s <table border=1 width="100%%">\n' % (t)
        t = ""
        for c in range(7):
            s = wnf_tools.cWochentageL[c]
            t = '%s <th width="14%%"> %s </th>\n' % (t, s)
        html = "%s <tr>%s</tr>\n" % (html, t)
        for z in range(4):
            t = ""
            w = 0
            for c in range(7):
                w = w + 1
                if (d == self.heute) and (self.FarbeHeute <> self.FarbeTransparent):
                    cl = self.FarbeHeute
                elif (wnf_tools.sFeiertag(d, self.Bundesland) <> "") and (self.FarbeFT <> self.FarbeTransparent):
                    cl = self.FarbeFT
                elif (w == 7) and (self.FarbeSO <> self.FarbeTransparent):
                    cl = self.FarbeSO
                elif (w == 6) and (self.FarbeSA <> self.FarbeTransparent):
                    cl = self.FarbeSA
                elif (self.FarbeNormal <> self.FarbeTransparent):
                    cl = self.FarbeNormal
                else:
                    cl = self.FarbeTransparent
                if cl == self.FarbeTransparent:
                    farbe = ''
                else:
                    farbe = ' bgcolor="%s"' % wnf_tools.RGBToHTML(cl)
                s = wnf_tools.DateToStr(d)
                t = '%s<td align=center %s><b> %s </b><br />\n' % (t, farbe, s)
                for i in range(4):
                    s = self.get_termin(d, i)
                    t = "%s%s<br />\n" % (t, s[0])
                d = d + difference1
                t = "%s</td>\n" % (t)
            html = "%s <tr>%s</tr>\n" % (html, t)
        html = "%s </table>" % (html)
        if aMitKopf:
            html = "%s </body></html>" % (html)
        return html

    def zeichne_kalender(self, im, x0, y0):
        d = self.von
        difference1 = datetime.timedelta(days=1)
        x = x0
        y = y0
        th = im.TextHeight + 4
        w = 0
        for c in range(7):
            w = w + 1
            im.rect(x, y, self.TagBreite, th)
            s = wnf_tools.cWochentageL[c]
            if (c == self.wochentag_i) and (self.FarbeHeute <> self.FarbeTransparent):
                im.text_box_c(x + 1, y + 1, self.TagBreite-2, th-2, s, self.FarbeHeute)
            elif (w == 7) and (self.FarbeSA <> self.FarbeTransparent):
                im.text_box_c(x + 1, y + 1, self.TagBreite-2, th-2, s, self.FarbeSO)
            elif (w == 6) and (self.FarbeSA <> self.FarbeTransparent):
                im.text_box_c(x + 1, y + 1, self.TagBreite-2, th-2, s, self.FarbeSA)
            elif (self.FarbeNormal <> self.FarbeTransparent):
                im.text_box_c(x + 1, y + 1, self.TagBreite-2, th-2, s, self.FarbeNormal)
            else:
                im.text_nc(x + 2, y + 2, self.TagBreite-2, s)
            x = x + self.TagBreite + self.TagRand
        y = y0 + th + self.TagRand
        for z in range(4):
            x = x0
            w = 0
            for c in range(7):
                w = w + 1
                cl = self.FarbeTransparent
                if (d == self.heute):
                    cl = self.FarbeHeute
                elif (wnf_tools.sFeiertag(d, self.Bundesland) <> ""):
                    cl = self.FarbeFT
                elif (w == 7):
                    cl = self.FarbeSO
                elif (w == 6):
                    cl = self.FarbeSA
                else:
                    cl = self.FarbeNormal
                if (cl <> self.FarbeTransparent):
                    im.rectclrand(x, y, self.TagBreite, self.TagHoehe, cl)
                else:
                    im.rect(x, y, self.TagBreite, self.TagHoehe)
                s = wnf_tools.DateToStr(d)
                im.text_b(x + 2, y + (2), s)
                im.text_box_c(x + 1, y + 2, self.TagBreite-2, th, s, cl)
                for i in range(4):
                    s, cl = self.get_termin(d, i)
                    if s <> "":
                        print d, s, cl
                        im.text_box_c(x + 1, y + (th * (i + 1)), self.TagBreite-2, th, s, cl)
                if (self.CountDown >= self.heute) and (self.CountDown >= d) and(d >= self.heute):
                    cd = self.CountDown -d
                    s = str(cd.days)
                    im.text_countdown(x, y, self.TagBreite, self.TagHoehe, s, self.CountDownFont, self.CountDownFontSize, self.FarbeCountDown)
                d = d + difference1
                x = x + self.TagBreite + self.TagRand
            y = y + self.TagHoehe + self.TagRand
        s = datetime.datetime.ctime(self.jetzt)
        im.text_n(x0 + 2, y0 + self.TagHoehe-th, s)


    def ausgabe_jpg(self, dn):
        im = wnf_image.TwnfImage(self.Breite, self.Hoehe, self.TextFont, self.TextFontSize, self.HGColor, self.TextColor, self.LineColor)
        if self.GrafikD <> "":
            im.hintergrundbild(0, 0, self.GrafikD)
        x0 = self.XOffset
        y0 = self.YOffset
        self.zeichne_kalender(im, x0, y0)
        im.save(dn)

    def ausgabe_jpg_ohne_hintergrund(self, dn):
        w = (self.TagBreite + self.TagRand) * 7;
        h = (self.TagHoehe + self.TagRand) * 4 + (self.TextFontSize + 2) * 1;
        im = wnf_image.TwnfImage(w, h, self.TextFont, self.TextFontSize, self.HGColor, self.TextColor, self.LineColor)
        x0 = 0
        y0 = 0
        self.zeichne_kalender(im, x0, y0)
        im.save(dn)

    def show_jpg(self):
        dn = wnf_tools.TempDateiname(".bmp")
        self.ausgabe_jpg(dn)
        wnf_tools.DateiStarten(dn)
        os.remove(dn)

    def eintragen_feiertage(self):
        d = self.von
        while (d <= self.bis):
            n = wnf_tools.sFeiertag(d, self.Bundesland)
            if n <> "":
                self.eintragen(d, n, self.FarbeFT)
            d = d + datetime.timedelta(days=1)


    def eintragen_termin(self, s):
        z = s.split(";")
        d = wnf_tools.StrToDate(z[0])
        n = z[1]
        c = z[2]
        cl = wnf_tools.PascalToRGB(c, wnf_tools.clWhite)
        if (d >= self.von) and (d <= self.bis):
            self.eintragen(d, n, cl)

    def eintragen_geburtstag(self, s):
        z = s.split(";")
        g = wnf_tools.StrToDate(z[0])
        n = z[1]
        c = z[2]
        cl = wnf_tools.PascalToRGB(c, wnf_tools.clYellow)
        dv = wnf_tools.DiesesJahr(g, self.von)
        db = wnf_tools.DiesesJahr(g, self.bis)
        if (dv >= self.von) and (dv <= self.bis):
            i = wnf_tools.AlterInJahren(g, self.von)
            n = "%i %s" % (i, n)
            self.eintragen(dv, n, cl)
        elif (db >= self.von) and (db <= self.bis):
            i = wnf_tools.AlterInJahren(g, self.bis)
            n = "%i %s" % (i, n)
            self.eintragen(db, n, cl)
            #zu Testzwecken zwei geburtstage an einem Tag
            #n = "%s xxx" % n
            #self.eintragen(db,n,cl)

    def eintragen_zeitraum(self, s):
        z = s.split(";")
        dv = wnf_tools.StrToDate(z[0])
        db = wnf_tools.StrToDate(z[1])
        n = z[2]
        c = z[3]
        cl = wnf_tools.PascalToRGB(c, wnf_tools.clWhite)
        if wnf_tools.zeitraum_ueberlappt(dv, db, self.von, self.bis):
            difference1 = datetime.timedelta(days=1)
            d = self.von
            for i in range(28):
                if (d >= dv) and (d <= db):
                    self.eintragen(d, n, cl)
                d = d + difference1

    def eintragen_zyklisch(self, s):
        z = s.split(";")
        g = wnf_tools.StrToDate(z[0])   #Anfangstermin
        t = wnf_tools.StrToInt(z[1])    #Wiederhalung alle t Tage
        n = z[2]                        #Name
        c = z[3]                        #Farbe
        cl = wnf_tools.PascalToRGB(c, wnf_tools.clYellow)
        while g < self.bis:
            if g>self.von:
                self.eintragen(g, n, cl)
            g = g + datetime.timedelta(t)

    def eintragen_multi(self, s):
        z = s.split(";")
        n = z[0]
        c = z[1]
        cl = wnf_tools.PascalToRGB(c, wnf_tools.clWhite)
        art = z[2]
        i = 0
        for dt in z:
            if (i > 2) and (dt <> ""):
                if dt.find("-") >= 0:
                    #Multitermin als Zeitraum von bis
                    t = dt.split("-")
                    dv = wnf_tools.StrToDate(t[0])
                    db = wnf_tools.StrToDate(t[1])
                    if wnf_tools.zeitraum_ueberlappt(dv, db, self.von, self.bis):
                        difference1 = datetime.timedelta(days=1)
                        d = self.von
                        for i in range(28):
                            if (d >= dv) and (d <= db):
                                self.eintragen(d, n, cl)
                                print n, dv, db
                            d = d + difference1
                else:
                    #einzelner Multitermin
                    d = wnf_tools.StrToDate(dt)
                    if (d >= self.von) and (d <= self.bis):
                        self.eintragen(d, n, cl)
                        print n, d
            i = i + 1

    def lese_str(self, ini, aSection, aName):
        try:
            s = ini.get(aSection, aName)
        except ConfigParser.NoOptionError:
            s = ""
        return s

    def lese_int(self, ini, aSection, aName, aDefault):
        s = self.lese_str(ini, aSection, aName)
        try:
            i = int(s)
        except:
            i = aDefault
        return i

    def lese_color(self, ini, aSection, aName, aDefault):
        s = self.lese_str(ini, aSection, aName)
        cl = wnf_tools.PascalToRGB(s, aDefault)
        return cl

    def lesen(self, dn):
        if os.path.exists(dn):
            ini = ConfigParser.ConfigParser()
            ini.read(dn)
            self.IniDateiname = dn
            self.Breite = ini.getint("Standard", "Breite")
            self.Hoehe = ini.getint("Standard", "Hoehe")
            self.TagBreite = ini.getint("Standard", "TagBreite")
            self.TagHoehe = ini.getint("Standard", "TagHoehe")
            self.TagRand = ini.getint("Standard", "TagRand")
            self.XOffset = ini.getint("Standard", "XOffset")
            self.YOffset = ini.getint("Standard", "YOffset")
            self.GrafikD = self.lese_str(ini, "Standard", "Linux_GrafikD")
            self.TextFont = self.lese_str(ini, "Standard", "Linux_TextFont")
            self.TextFontSize = self.lese_int(ini, "Standard", "Linux_TextFont_Size", self.TextFontSize)
            self.CountDownFont = self.lese_str(ini, "Standard", "Linux_CountDownFont")
            self.CountDownFontSize = self.lese_int(ini, "Standard", "Linux_CountDownFont_Size", self.CountDownFontSize)
            self.FarbeCountDown = self.lese_color(ini, "Standard", "FarbeCountDown", self.FarbeCountDown)
            self.FarbeHeute = self.lese_color(ini, "Standard", "FarbeHeute", self.FarbeHeute)
            self.FarbeFT = self.lese_color(ini, "Standard", "FarbeFT", self.FarbeFT)
            self.FarbeSA = self.lese_color(ini, "Standard", "FarbeSA", self.FarbeSA)
            self.FarbeSO = self.lese_color(ini, "Standard", "FarbeSO", self.FarbeSO)
            self.FarbeNormal = self.lese_color(ini, "Standard", "FarbeNormal", self.FarbeNormal)
            self.FarbeTransparent = self.lese_color(ini, "Standard", "FarbeTransparent", self.FarbeTransparent)
            self.Bundesland = self.lese_str(ini, "Standard", "Bundesland")
            self.eintragen_feiertage()
            try:
                for x in ini.items('Termine'):
                    self.eintragen_termin(x[1])
            except ConfigParser.NoSectionError:
                print 'Keine Termine'
            try:
                for x in ini.items('Geburtstage'):
                    self.eintragen_geburtstag(x[1])
            except ConfigParser.NoSectionError:
                print 'Keine Jahrestage'
            try:
                for x in ini.items('Zeitraum'):
                    self.eintragen_zeitraum(x[1])
            except ConfigParser.NoSectionError:
                print 'Kein Zeitraum'
            try:
                for x in ini.items('Zyklisch'):
                    self.eintragen_zyklisch(x[1])
            except ConfigParser.NoSectionError:
                print 'Keine zyklischen Termine'
            try:
                for x in ini.items('Multi'):
                    self.eintragen_multi(x[1])
            except ConfigParser.NoSectionError:
                print 'Keine Multitermine'
            return True
        else:
            return False

    def SetWallpaper(self, dn):
        s = 'dcop kdesktop KBackgroundIface setWallpaper %s 2' % (dn)
        os.system(s)
        # print s

if __name__ == "__main__":
    #ini = os.environ["HOME"]
    #ini = "%s/.wnfdesktopkalender/wnfDesktopKalender.ini" % (ini)
    #ini = "/wnfdaten/wine/Eigene_Dateien/wnfDesktopKalender/wnfDesktopKalender.ini"
    ini = "/wnfdaten/Downloads/wnfDesktopKalender.ini"
    dn = '/tmp/wnfDesktopkalender.jpg'
    t = TwnfDesktopKalender()
    print t.caption
    print "Auswerten von ", ini
    if t.lesen(ini):
        #t.ausgabe_jpg_ohne_hintergrund(dn)
        t.ausgabe_jpg(dn)
        #t.ausgabe_jpg(dn)
        #t.show_jpg()
        #print t.ausgabe_html(False)
        print "Ausgabe von ", dn
        print "ende"
