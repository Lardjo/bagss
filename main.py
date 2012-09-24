#!usr/bin/env python3
# File: main.py
# Main File

import os
import plugin
import path

s = ""

print ("\n")
print ("BAGSS v0.1 Beta")
print ("\nHi,",path.UserName,"!\n")

# Checking existence of directory 'Backup'
#
print ("Сhecking the backup folder...")

if os.path.exists("Backup") == True:

	print ("Success!") # All right

else:

	print ("Backup dir not found! Creating folder...")

	os.mkdir("Backup") # Create folder

	print ("Backup folder created!\n")
#
# -- END Checking existence of directory 'Backup' --

# Loading all plugins
#
print ("Loading plugins...")

plugin.LoadPlugins()

print ("Loading complete!")
#
# -- END Loading all plugins --

print ("\nTo Start backup type 'backup' and press Enter...")
print ("...or type 'exit' for exit.")

while (s != 'exit'):

    s = input()
    a = s.split(" ")

    for p in plugin.Plugins:

        p.OnCommand(a[0])
