#!usr/bin/env python3
# Plugin System

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
            #print ("Found plugin", pluglist)
            mod = __import__("plugins."+os.path.splitext(pluglist)[0])   
        except ImportError:
            pass
        
    for plugin in Plugin.__subclasses__():
        p = plugin()
        Plugins.append(p)
        p.OnLoad()

    return