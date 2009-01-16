#!/usr/bin/env python

#############################################################################
# wnfpy_test_qt - PyQT application template for KDevelop
#
# Translated from C++ qmakeapp.cpp
# (qmakeapp.cpp - Copyright (C) 1992-2002 Trolltech AS.  All rights reserved.)
#
# This file is part of an example program for Qt.  This example
# program may be used, distributed and modified without limitation.
#
#############################################################################

import sys
import os.path
from qt import *

class wnfpy_test_qt(QMainWindow):
    """An application called wnfpy_test_qt."""

    def __init__(self):
        QMainWindow.__init__(self, None, "wnfpy_test_qt")
#        self.initIcons()
#        self.setup()
#        self.initPrinter()
#        self.initToolBar()
#        self.initMenu()
#        self.initMainWidget()
#        self.setCaption(self.appTitle)


def main(args):
    app=QApplication(args)
    mainWindow = wnfpy_test_qt()
    mainWindow.show()
    app.connect(app, SIGNAL("lastWindowClosed()"), app, SLOT("quit()"))
    app.exec_loop()



if __name__ == "__main__":
    main(sys.argv)
