#!usr/bin/env python3
# File: package.py
# Package System

import os
import tarfile
   
def PackageSystem(source, gname):

    try:

        targetBackup = (gname + ".tar.gz")
        tar = tarfile.open(os.path.join(".","backup", targetBackup), "w:gz")
        tar.add(source, arcname=gname)
        tar.close()

    except TypeError:
        
        print ("Backup fail!")

def UnPackageSystem(source, gname):

	try:

		targetReBackup = (gname + ".tar.gz")
		tar = tarfile.open(os.path.join(".", "backup", targetReBackup), "r:gz")
		tar.extractall(source)
		tar.close()

	except TypeError:

		print ("Restore fail!")