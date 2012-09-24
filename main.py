#!usr/bin/env python3
# Main File

import os
import plugin
import path

s = ""

print ("\n")
print ("**************************************************************")
print ("*                        _v1.0 Alpha_                        *")
print ("**************************************************************")
print ("\nHi,",path.UserName,"!\n")
print ("Loading plugins...")
print ("------------------")

plugin.LoadPlugins()

print ("-----------------")
print ("Loading complete!")
print ("\nTo Start backup type 'backup' and press Enter...")
print ("...or type 'exit' for exit.")

while (s != 'exit'):

    s = input()
    a = s.split(" ")

    for p in plugin.Plugins:

        p.OnCommand(a[0])
