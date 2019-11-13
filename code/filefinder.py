import os
import re
#import win32api

def find_file(root_folder, rex):
    for root,dirs,files in os.walk(root_folder):
        for f in files:
            result = rex.search(f)
            if result:
                return(os.path.join(root, f))
                #break # if you want to find only one

"""
def find_file_in_all_drives(file_name):
    #create a regular expression for the file
    rex = re.compile(file_name)
    for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
        find_file( drive, rex )
"""

#find_file_in_all_drivers( '4ed\.exe' )
def find_4ed():
    rex = re.compile('4ed\.exe' )
    return find_file('C:\\', rex)
