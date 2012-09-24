#!usr/bin/env python3
# Package System

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