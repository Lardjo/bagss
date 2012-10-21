#!usr/bin/env python3
# File: nfshp.py
# Game Name: Need for Speed Hot Pursuit

import os
import sys

sys.path.append('../')

from plugin import Plugin
from path import DocumentsPath
from package import Package
from package import UnPackage

class HotPursuitPlugin(Plugin):

    Name = "Need for Speed(TM) Hot Pursuit"
    Author = "Konstantin N."
    SupportOS = ["Windows"] #key-words: Windows, Linux, Darwin

    def OnLoad(self):
        pass
        
    def OnCommand(self):

        path = os.path.join(DocumentsPath, "Criterion Games", "Need for Speed(TM) Hot Pursuit")
        name = "Need for Speed(TM) Hot Pursuit"
        Package(source=path, gname=name)

    def OnRestore(self):

    	path = os.path.join(DocumentsPath, "Criterion Games")
    	name = "Need for Speed(TM) Hot Pursuit"
    	UnPackage(source=path, gname=name)