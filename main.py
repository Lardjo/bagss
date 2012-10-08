#!usr/bin/env python3
# File: main.py
# Main File

import os
import sys
import plugin
import path

sys.path.append('../')

from BAGSS import __version__

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
    info = "Succes!"

except IOError:

    info = "Error!"

print ("Checking load plugins... {0}".format(info))

# END Loading all plugins

print ("""
To Start backup type 'backup' and press Enter...
...or type 'exit' for exit.""")

while (s != 'exit'):

    s = input()
    a = s.split(" ")
    ib = 0

    if s == 'backup':

        print ("Start backup...")

        for p in plugin.Plugins:

            p.OnCommand()
            ib += 1

        print ("Backup {0} games complite!".format(ib))

    else:

        pass