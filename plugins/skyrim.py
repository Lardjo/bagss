#!usr/bin/env python3
# File: nfshp.py
# Game Name: The Elder Scrolls V: Skyrim

import os
import sys

sys.path.append('../')

from plugin import Plugin
from path import DocumentsPath
from package import PackageSystem

class NFSHPPlugin(Plugin):

    Name = "TESV:Skyrim"
    Author = "Lardjo"
    SupportOS = ["Windows"] #key-words: Windows, Linux, Darwin

    def OnLoad(self):
        pass
        
    def OnCommand(self):

        GamePath = os.path.join (DocumentsPath, "my games", "skyrim")
        GameName = "The_Elder_Scrolls_V_Skyrim"
        PackageSystem(source=GamePath, gname=GameName)