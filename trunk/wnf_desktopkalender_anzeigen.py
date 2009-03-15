#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import sys
import datetime
import wnf_tools
import wnf_desktopkalender_object

#fontname = "/usr/share/fonts/truetype/freefont/FreeSans.ttf"
#Fontname = "/usr/share/fonts/truetype/msttcorefonts/verdana.ttf"
#GrafikD = "/wnfdaten/wine/Eigene_Bilder/Wallpaper/www_soc_com/200810011842-5490.jpg"
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
            #t.ausgabe_28()
            #wallpaper = "%s/wnfdesktopkalender.svg" % (zpfad)
            #t.ausgabe_svg(wallpaper)
            #print wallpaper
            wallpaper = "%s/wnfdesktopkalender.bmp" % (zpfad)
            print "Anzeigen von ",wallpaper
            t.ausgabe_jpg(wallpaper)
            t.SetWallpaper(wallpaper)
        else:
            print "Die Datei %s existiert nicht." % ini
    else:
        print "Keine Zugriffsrechte auf das Verzeichnis %s " % (zpfad)

if __name__ == "__main__":
    main(sys.argv)
