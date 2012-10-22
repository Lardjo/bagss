#!usr/bin/env python3
#
# Copyright (c) 2012
#
# This file is part of BAGSS, and is made available under the
# 3-clause BSD license. See LICENSE for the full details.

import os

from winreg import HKEY_CURRENT_USER, OpenKey, QueryValueEx

SteamGamesPath = None    # Steam Common Directory
DocumentsPath = None     # Windows My Documents Directory
GamesPath = None         # Windows My Games Directory
LocalAppPath = None      # Windows Local Data Directory 

try:

    key = OpenKey(HKEY_CURRENT_USER, 'Software\\Valve\\Steam')
    SteamPath = QueryValueEx(key, 'SteamPath') [0]
    SteamGamesPath = os.path.normcase(os.path.join(SteamPath, 'steamapps', 'common'))

except WindowsError:
    pass

try:

    key = OpenKey(HKEY_CURRENT_USER, 'Volatile Environment')
    UserPath = QueryValueEx(key, 'USERPROFILE') [0]
    DocumentsPath = os.path.normcase(os.path.join(UserPath, 'Documents'))

except WindowsError:
    pass

try:

    key = OpenKey(HKEY_CURRENT_USER, 'Volatile Environment')
    UserPath = QueryValueEx(key, 'USERPROFILE') [0]
    GamesPath = os.path.normcase(os.path.join(UserPath, 'Saved Games'))

except WindowsError:
    pass

try:

    key = OpenKey(HKEY_CURRENT_USER, 'Volatile Environment')
    LocalApp = QueryValueEx(key, 'LOCALAPPDATA') [0]
    LocalAppPath = os.path.normcase(os.path.join(LocalApp))

except WindowsError:
    pass