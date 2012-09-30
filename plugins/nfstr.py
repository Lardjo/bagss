#!usr/bin/env python3
# File: nfstr.py
# Game Name: Need for Speed The Run

__version__ = "0.1.0"
__author__ = "Konstantin N."
__copyright__ = "2012 (с) Network Sys."

import os
import sys

sys.path.append('../')

from plugin import Plugin
from path import DocumentsPath
from package import PackageSystem

class NFSTRPlugin(Plugin):

    Name = "NFSTR"

    def OnLoad(self):

        print ("NFS The Run: Plugin Loaded!")
        
    def OnCommand(self,cmd):

        if (cmd == 'backup'):

            GamePath = os.path.join (DocumentsPath, "NFSTR")
            GameName = "Need_for_Speed_The_Run"
            PackageSystem(source=GamePath, gname=GameName)

            return True

        else:

            return False