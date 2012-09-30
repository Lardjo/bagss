#!usr/bin/env python3
# File: package.py
# Package System

__version__ = "0.1.0"
__author__ = "Konstantin N."
__copyright__ = "2012 (с) Network Sys."

import os
import sys
import tarfile
import time
import plugin

source = None
      
def PackageSystem(source, gname):

    destination = gname

    try:

        targetBackup = (destination + time.strftime(" (%Y.%m.%d_%H.%M.%S)") + ".tar.gz")
        tar = tarfile.open(os.path.join(".","backup", targetBackup), "w:gz")
        tar.add(source)
        tar.close()
        print ("Backup Complete!")

    except TypeError:
        
        print ("Backup fail!")    