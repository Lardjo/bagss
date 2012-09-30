#!usr/bin/env python3
# File: nfshp.py
# Game Name: Need for Speed Hot Pursuit

__version__ = "0.1.0"
__author__ = "Konstantin N."
__copyright__ = "2012 (с) Network Sys."

import os
import sys

sys.path.append('../')

from plugin import Plugin
from path import DocumentsPath
from package import PackageSystem

class NFSHPPlugin(Plugin):

    Name = "NFSHP"

    def OnLoad(self):

        print ("NFS Hot Pursuit 2010: Plugin Loaded!")
        
    def OnCommand(self,cmd):

        if (cmd == 'backup'):

            GamePath = os.path.join (DocumentsPath, "Criterion Games", "Need for Speed(TM) Hot Pursuit")
            GameName = "Need_for_Speed_Hot_Pursuit"
            PackageSystem(source=GamePath, gname=GameName)

            return True

        else:

            return False