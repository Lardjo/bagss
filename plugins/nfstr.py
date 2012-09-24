#!usr/bin/env python3
# nfstr.py
# Plugin version: v1.0 Beta 1
# Game Name: Need for Speed The Run

import os
import sys

sys.path.append('../')

from plugin import Plugin
from path import DocumentsPath
from package import PackageSystem

class NFSTRPlugin(Plugin):

    Name = "NFSTR"
    Author = "Lardjo"

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