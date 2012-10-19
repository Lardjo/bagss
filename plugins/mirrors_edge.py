#!usr/bin/env python3
# File: nfshp.py
# Game Name: Mirror's Edge

import os
import sys

sys.path.append('../')

from plugin import Plugin
from path import DocumentsPath
from package import PackageSystem
from package import UnPackageSystem

class NFSHPPlugin(Plugin):

    Name = "Mirror's Edge"
    Author = "Lardjo"
    SupportOS = ["Windows"] #key-words: Windows, Linux, Darwin

    def OnLoad(self):
        pass
        
    def OnCommand(self):

        GPath = os.path.join(DocumentsPath, "EA Games", "Mirror's Edge")
        GName = "Mirror's Edge"
        PackageSystem(source=GPath, gname=GName)

    def OnRestore(self):

    	GPath = os.path.join(DocumentsPath, "EA Games")
    	GName = "Mirror's Edge"
    	UnPackageSystem(source=GPath, gname=GName)