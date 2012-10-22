#!usr/bin/env python3
#
# Copyright (c) 2012
#
# This file is part of BAGSS, and is made available under the
# 3-clause BSD license. See LICENSE for the full details.

import os
import sys
import path

sys.path.append('../')

from bagss import plugin
from bagss import __version__

s = ""

print ("""
================================	
        BAGSS v%s
================================
""" % __version__)

print ("Hi, %s!\n" % path.UserName)

# Checking existence of directory Backup

if os.path.exists("Backup"):

	info = "Success!"

else:

	try:

		os.mkdir("Backup")
		info = "Not found. Create a folder"

	except OSError:

		info = "Error! Folder not created!"

print ("Checking the backup folder... {0}".format(info))

# END Checking existence of directory Backup

# Loading all plugins

try:

    plugin.LoadPlugins()
    info = "Success!"

except IOError:

    info = "Error!"

print ("Checking load plugins... Loaded {0} plugins... {1}".format(len(plugin.Plugins), info))

# END Loading all plugins

print ("""
To Start backup type 'backup' or type 'restore' for restore all files...
...or type 'exit' for exit.""")

while (s != 'exit'):

    s = input()
    a = s.split(" ")
    i = 0

    if s == 'backup':

        print ("Start backup...")

        for p in plugin.Plugins:

            p.OnCommand()
            i += 1

        print ("Backup {0} games complite!".format(i))

    elif s == 'restore':

        print ("Start restore...")

        for p in plugin.Plugins:

            p.OnRestore()
            i += 1

        print ("Restore {0} games complite!".format(i))

    else:

        pass