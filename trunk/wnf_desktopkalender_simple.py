#! /usr/bin/python
# -*- coding: UTF-8 -*-

__author__="wnf"
__date__ ="$28.02.2009 06:39:03$"

import os
import sys
import datetime
import wnf_tools
import wnf_desktopkalender_object

#Das ist die Standard-Ini-Datei des Entwicklers
#Der Anwender sollte seine Ini-Datei als  Parameter übergeben
IniDatei = "/wnfdaten/wine/Eigene_Dateien/wnfDesktopKalender/wnfDesktopKalender.ini"

def main(args):
    zpfad = os.environ["HOME"]
    zpfad = "%s/.wnfdesktopkalender" % (zpfad)
    if wnf_tools.forceDir(zpfad):
        d = datetime.date.today()
        t=wnf_desktopkalender_object.TwnfDesktopKalender(d)
        print t.caption
        #Entweder das Inifile wird als erster Parameter übegeben
        ini=wnf_tools.paramStr(args,1)
        if ini=="":
            #oder es wird das Standard Ini-File verwendet
            ini = IniDatei
        print "Auswerten von ",ini
        if t.lesen(ini):
            if t.GrafikD=="":
                print "Es wird keine Hintergrundgrafik verwendet. Linux_GrafikD ist leer"
            if t.TextFont=="":
                print "Es wird kein Textfont verwendet. Linux_TextFont ist leer"
            print t.TextFont
            #t.ausgabe_28()
            #wallpaper = "%s/wnfdesktopkalender.svg" % (zpfad)
            #t.ausgabe_svg(wallpaper)
            #print wallpaper
            wallpaper = "%s/wnfdesktopkalender_simple.png" % (zpfad)
            print "Erstellen von ",wallpaper
            t.ausgabe_jpg_ohne_hintergrund(wallpaper)
            #t.SetWallpaper(wallpaper)
        else:
            print "Die Datei %s existiert nicht." % ini
    else:
        print "Keine Zugriffsrechte auf das Verzeichnis %s " % (zpfad)

if __name__ == "__main__":
    main(sys.argv)
