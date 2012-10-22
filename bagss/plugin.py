#!usr/bin/env python3
#
# Copyright (c) 2012
#
# This file is part of BAGSS, and is made available under the
# 3-clause BSD license. See LICENSE for the full details.

import os
import platform

Plugins = []
s = platform.system()

class Plugin(object):

    Name = "BAGSS"

    def OnLoad(self):
        pass

    def OnCommand(self):
        pass

    def OnRestore(self):
        pass

def LoadPlugins():

    plug = os.listdir('./plugins')

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

                print ("Plugin {0} not supported on your {1}".format(plugin.Name, s))

        except KeyError:

            print ("Error!")

    return