#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="wnf"
__date__ ="$16.09.2009 16:27:58$"

import os
import ConfigParser
import datetime
import wnf_tools
from icalendar import Calendar, Event
from icalendar import UTC # timezone

class TwnfDesktopKalender_to_ics:
    """
    Ausgabe der Termine aus wnfDesktopkalender in eine ics Datei
    """

    def __init__(self):
        self.IniDateiname = ''

    def lesen(self, dn):
        if os.path.exists(dn):
            ini = ConfigParser.ConfigParser()
            ini.read(dn)
            return True
        else:
            return False

    def ausgabe_ics(self, dn):
        print "Ausgabe von ", dn
        cal = Calendar()
        cal.add('prodid', '-//wnfDesktopKalender//wlsoft.de//')
        cal.add('version', '2.0')

        event = Event()
        event.add('summary', 'Python meeting about calendaring')
        event.add('dtstart', wnf_tools.strToDate('03.04.2009'))
        event.add('dtend', wnf_tools.strToDate('03.04.2009'))
        event.add('dtstamp', wnf_tools.strToDate('03.04.2009'))
        event['uid'] = '20050115T101010/27346262376@mxm.dk'
        event.add('priority', 5)

        cal.add_component(event)

        f = open(dn, 'wb')
        f.write(cal.as_string())
        f.close()

if __name__ == "__main__":
    ini = "/wnfdaten/wine/Eigene_Dateien/wnfDesktopKalender/wnfDesktopKalender.ini"
    dn = '/tmp/wnfDesktopkalender.ics'
    t = TwnfDesktopKalender_to_ics()
    print "Auswerten von ", ini
    if t.lesen(ini):
        t.ausgabe_ics(dn)
        print "ende"
