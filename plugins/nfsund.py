#!usr/bin/env python3
# File: nfstr.py
# Game Name: Need for Speed: Undercover

import os
import sys

sys.path.append('../')

from plugin import Plugin
from path import DocumentsPath
from package import PackageSystem

class NFSTRPlugin(Plugin):

    Name = "NFS:Undercover"
    Author = "Lardjo"
    SupportOS = ["Windows"] #key-words: Windows, Linux, Darwin

    def OnLoad(self):
        pass
        
    def OnCommand(self):

        GamePath = os.path.join (DocumentsPath, "NFS Undercover")
        GameName = "Need_For_Speed_Undercover"
        PackageSystem(source=GamePath, gname=GameName)