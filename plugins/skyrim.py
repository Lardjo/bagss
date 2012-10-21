#!usr/bin/env python3
# File: nfshp.py
# Game Name: The Elder Scrolls V: Skyrim

import os
import sys

sys.path.append('../')

from plugin import Plugin
from path import DocumentsPath
from package import Package
from package import UnPackage

class SkyrimPlugin(Plugin):

    Name = "The Elder Scrolls V Skyrim"
    Author = "Konstantin N."
    SupportOS = ["Windows"] #key-words: Windows, Linux, Darwin

    def OnLoad(self):
        pass
        
    def OnCommand(self):

        path = os.path.join (DocumentsPath, "my games", "skyrim")
        name = "The Elder Scrolls V Skyrim"
        Package(source=path, gname=name)

    def OnRestore(self):

    	path = os.path.join (DocumentsPath, "my games")
    	name = "The Elder Scrolls V Skyrim"
    	UnPackage(source=path, gname=name)