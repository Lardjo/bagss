#!usr/bin/env python3
# File: nfshp.py
# Game Name: Mirror's Edge

import os
import sys

sys.path.append('../')

from plugin import Plugin
from path import DocumentsPath
from package import Package
from package import UnPackage

class MirrorsPlugin(Plugin):

    Name = "Mirror's Edge"
    Author = "Konstantin N."
    SupportOS = ["Windows"] #key-words: Windows, Linux, Darwin

    def OnLoad(self):
        pass
        
    def OnCommand(self):

        path = os.path.join(DocumentsPath, "EA Games", "Mirror's Edge")
        name = "Mirror's Edge"
        Package(source=path, gname=name)

    def OnRestore(self):

    	path = os.path.join(DocumentsPath, "EA Games")
    	name = "Mirror's Edge"
    	UnPackage(source=path, gname=name)