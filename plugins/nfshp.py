#!usr/bin/env python3
# File: nfshp.py
# Game Name: Need for Speed Hot Pursuit

import os
import sys

sys.path.append('../')

from plugin import Plugin
from path import DocumentsPath
from package import PackageSystem

class NFSHPPlugin(Plugin):

    Name = "NFS:HP"
    Author = "Lardjo"
    SupportOS = ["Windows"] #key-words: Windows, Linux, Darwin

    def OnLoad(self):
        pass
        
    def OnCommand(self):

        GamePath = os.path.join (DocumentsPath, "Criterion Games", "Need for Speed(TM) Hot Pursuit")
        GameName = "Need_for_Speed_Hot_Pursuit"
        PackageSystem(source=GamePath, gname=GameName)