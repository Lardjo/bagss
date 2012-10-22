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

class TheRunPlugin(Plugin):

    Name = "Need for Speed(TM) The Run"
    Author = "Konstantin N."
    SupportOS = ["Windows"] #key-words: Windows, Linux, Darwin

    def OnLoad(self):
        pass
        
    def OnCommand(self):

        path = os.path.join(DocumentsPath, "NFSTR")
        name = "Need for Speed(TM) The Run"
        Package(source=path, gname=name)

    def OnRestore(self):

    	path = DocumentsPath
    	name = "Need for Speed(TM) The Run"
    	UnPackage(source=path, gname=name)