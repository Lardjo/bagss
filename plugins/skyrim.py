#!usr/bin/env python3
#
# Copyright (c) 2012
#
# This file is part of BAGSS, and is made available under the
# 3-clause BSD license. See LICENSE for the full details.

import os
import sys

from bagss.plugin import Plugin
from bagss.path import DocumentsPath
from bagss.package import Package
from bagss.package import UnPackage

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