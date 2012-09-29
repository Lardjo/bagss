#!usr/bin/env python3
# File: plugin.py
# Plugin System v1

import os
import sys
import platform


Plugins = []
s = platform.system()


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

        try:

            if s in plugin.SupportOS:

                p = plugin()
                Plugins.append(p)
                p.OnLoad()

            else:

                print ("Plugin for {} not supported on your PC".format(plugin.Name))

        except KeyError:

            print ("Error 0x001")

    return