#!usr/bin/env python3
# File: nfstr.py
# Game Name: Need for Speed: Undercover

import os
import sys

sys.path.append('../')

from plugin import Plugin
from path import DocumentsPath
from package import Package
from package import UnPackage

class UndercoverPlugin(Plugin):

    Name = "Need for Speed(TM) Undercover"
    Author = "Konstantin N."
    SupportOS = ["Windows"] #key-words: Windows, Linux, Darwin

    def OnLoad(self):
        pass
        
    def OnCommand(self):

        path = os.path.join(DocumentsPath, "NFS Undercover")
        name = "Need for Speed(TM) Undercover"
        Package(source=path, gname=name)

    def OnRestore(self):

    	path = DocumentsPath
    	name = "Need for Speed(TM) Undercover"
    	UnPackage(source=path, gname=name)