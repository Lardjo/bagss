#!usr/bin/env python3
# Path file

import os
import sys


from winreg import HKEY_CURRENT_USER, OpenKey, QueryValueEx


SteamGamesPath = None    # Steam Common Directory
DocumentsPath = None     # Windows My Documents Directory
GamesPath = None         # Windows My Games Directory
LocalAppPath = None      # Windows Local Data Directory 
UserName = None          # User Name

#backupDir = os.path.abspath(os.curdir + "/backup")  #Backup Directory

# Get All Path

try:

    key = OpenKey(HKEY_CURRENT_USER, 'Software\\Valve\\Steam')
    SteamPath = QueryValueEx(key, 'SteamPath') [0]
    SteamGamesPath = os.path.normcase(os.path.join(SteamPath, 'steamapps', 'common'))


    key = OpenKey(HKEY_CURRENT_USER, 'Volatile Environment')
    UserPath = QueryValueEx(key, 'USERPROFILE') [0]
    DocumentsPath = os.path.normcase(os.path.join(UserPath, 'Documents'))
    GamesPath = os.path.normcase(os.path.join(UserPath, 'Saved Games'))


    key = OpenKey(HKEY_CURRENT_USER, 'Volatile Environment')
    LocalApp = QueryValueEx(key, 'LOCALAPPDATA') [0]
    LocalAppPath = os.path.normcase(os.path.join(LocalApp))


    key = OpenKey(HKEY_CURRENT_USER, 'Volatile Environment')
    UserName = QueryValueEx(key, 'USERNAME') [0]

except WindowsError:
    pass