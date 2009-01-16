#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#http://kinterbasdb.sourceforge.net/dist_docs/usage.html#adv_prog_maint_servapi_connect
#sudo apt-get install python-kinterbasdb
import sys
import kinterbasdb; kinterbasdb.init(type_conv=0)
import kinterbasdb.services
import wnf_tools

# Encoding der Standardausgabe herausfinden
stdout_encoding = sys.stdout.encoding or sys.getfilesystemencoding()

class TwnfFIBDatabase:
    def __init__(self,aServer,aDatenbank,aUser,aPasswort):
        self.Server=aServer
        self.Datenbank=aDatenbank
        self.User=aUser
        self.Passwort=aPasswort

    def ZeigeStatus(self):
        print "Server                : %s" % self.Server
        print "Datenbank             : %s" % self.Datenbank
        print "User                  : %s" % self.User
        print "Passwort              : %s" % self.Passwort
        print "ServiceManagerVersion : %s" % self.svc.getServiceManagerVersion()
        print "ServerVersion         : %s" % self.svc.getServerVersion()
        print "Architecture          : %s" % self.svc.getArchitecture()
        print "Firebird-Verzeichnis  : %s" % self.svc.getHomeDir()
#        print "ConnectionCount       : %i" % self.svc.getConnectionCount()

    def connect(self):
        self.svc = kinterbasdb.services.connect(host=self.Server, user=self.User, password=self.Passwort)
        dsn="%s:/%s" % (self.Server,self.Datenbank)
        self.con = kinterbasdb.connect(dsn=dsn, user=self.User, password=self.Passwort)
        return True

    def list_Adr(self):
        print "="*70
        dt_Adr = self.con.cursor()
        dt_Adr.execute("SELECT ID,KURZ,STR,TEL1 FROM KO_ADR ORDER BY STR")
        rows = dt_Adr.fetchall()
        for row in rows:
            s = unicode("%3i %10s %10s" % (row[0], row[2], row[1]), 'iso-8859-1')
            print s.encode(stdout_encoding)
        print "="*70


if __name__ == "__main__":
    db=TwnfFIBDatabase("localhost","/var/lib/firebird/2.0/data/wnfKontakt.fdb","SYSDBA","wlsoft")
#    db=TwnfFIBDatabase("debian10","/wnfdaten/Datenbanken/wnfDSL.fdb","SYSDBA","wlsoft")
    if db.connect():
        db.ZeigeStatus()
        db.list_Adr()
        print "ende"
