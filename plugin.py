#!usr/bin/env python3
# File: plugin.py
# Plugin System

import os
import platform

Plugins = []
s = platform.system()

class Plugin(object):

    Name = "BAGSS"

    def OnLoad(self):
        pass

    def OnCommand(self, cmd):
        pass

def LoadPlugins():

    plug = os.listdir('plugins')

    il = 0

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
                il += 1

            else:

                print ("Plugin {0} not supported on your {1}".format(plugin.Name, s))

        except KeyError:

            print ("Error 0x001")

    return