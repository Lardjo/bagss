#!usr/bin/env python3
# File: plugin.py
# Plugin System

__version__ = "0.1.0"
__author__ = "Konstantin N."
__copyright__ = "2012 (с) Network Sys."

import os
import sys


Plugins = []


class Plugin(object):

    Name = "BAGSS"
    Author = "Lardjo"

    def OnLoad(self):
        pass

    def OnCommand(self, cmd):
        pass


def LoadPlugins():
    
    plug = os.listdir('plugins')

    for pluglist in plug:

        try:

            mod = __import__("plugins."+os.path.splitext(pluglist)[0])

        except ImportError:
            pass
        
    for plugin in Plugin.__subclasses__():
        
        p = plugin()
        Plugins.append(p)
        p.OnLoad()

    return