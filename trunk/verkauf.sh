#!/bin/bash
echo "Verkauf des wnfDesktopkalenders"
cd /home/wnf/python/wnfDesktopkalender/
tar -cp -f wnfDesktopkalender.tar *.py
7za a -t7z wnfDesktopkalender.7z wnfDesktopkalender.tar > null
rm wnfDesktopkalender.tar
7za l wnfDesktopkalender.7z
ls -lh *.7z

