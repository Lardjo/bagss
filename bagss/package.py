#!usr/bin/env python3
#
# Copyright (c) 2012
#
# This file is part of BAGSS, and is made available under the
# 3-clause BSD license. See LICENSE for the full details.

import os
import tarfile
   
def Package(source, gname):

    try:

        targetBackup = (gname + ".tar.gz")
        tar = tarfile.open(os.path.join(".","backup", targetBackup), "w:gz")
        tar.add(source, os.path.basename(source))
        tar.close()

    except TypeError:
        
        print ("Backup fail!")

def UnPackage(source, gname):

	try:

		targetReBackup = (gname + ".tar.gz")
		tar = tarfile.open(os.path.join(".", "backup", targetReBackup), "r:gz")
		tar.extractall(source)
		tar.close()

	except TypeError:

		print ("Restore fail!")