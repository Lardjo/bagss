#!usr/bin/env python3
# File: package.py
# Package System

import os
import tarfile
import time
   
def PackageSystem(source, gname):

    try:

        targetBackup = (gname + time.strftime(" (%Y.%m.%d_%H.%M.%S)") + ".tar.gz")
        tar = tarfile.open(os.path.join(".","backup", targetBackup), "w:gz")
        tar.add(source)
        tar.close()

    except TypeError:
        
        print ("Backup fail!")