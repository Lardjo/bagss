#!usr/bin/env python3
# File: package.py
# Package System

import os
import tarfile
import time

source = None
      
def PackageSystem(source, gname):

    destination = gname

    try:

        targetBackup = (destination + time.strftime(" (%Y.%m.%d_%H.%M.%S)") + ".tar.gz")
        tar = tarfile.open(os.path.join(".","backup", targetBackup), "w:gz")
        tar.add(source)
        tar.close()
        #print ("Backup Complete!")

    except TypeError:
        
        print ("Backup fail!")    