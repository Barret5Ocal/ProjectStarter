import os
import re
from multiprocessing import Process, Queue, Event

def find_file(root_folder, rex):
    for root,dirs,files in os.walk(root_folder):
        for f in files:
            result = rex.search(f)
            if result:
                return(os.path.join(root, f))
                break # if you want to find only one
                
def find_file_multi(root_folder, rex, queue, quit, foundit):
    for root,dirs,files in os.walk(root_folder):
        if not quit.is_set():
            for f in files:
                result = rex.search(f)
                if result:
                    queue.put(os.path.join(root, f))
                    foundit.set()
                    break # if you want to find only one
        else:
            break
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


def find_4ed_fast():
    rex = re.compile('4ed\.exe' )
    dir_list = next(os.walk('C:\\'))[1]
    jobs = []
    queue = Queue()
    quit = Event()
    foundit = Event()
    for dir in dir_list:
        if dir != '$Recycle.Bin':
            p = Process(target=find_file_multi, args=('C:\\'+dir+'\\',rex, queue, quit, foundit))   
            jobs.append(p)
            p.start()
    foundit.wait()  
    quit.set()   
    return queue.get()