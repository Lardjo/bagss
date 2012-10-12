#!usr/bin/env python3
# File: nfshp.py
# Game Name: Mirror's Edge

import os
import sys

sys.path.append('../')

from plugin import Plugin
from path import DocumentsPath
from package import PackageSystem

class NFSHPPlugin(Plugin):

    Name = "Mirror's Edge"
    Author = "Lardjo"
    SupportOS = ["Windows"] #key-words: Windows, Linux, Darwin

    def OnLoad(self):
        pass
        
    def OnCommand(self):

        GamePath = os.path.join (DocumentsPath, "EA Games", "Mirror's Edge")
        GameName = "Mirrors_Edge"
        PackageSystem(source=GamePath, gname=GameName)