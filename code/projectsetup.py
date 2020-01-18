import os
import sys

import filecontent
import filefinder

if __name__ == "__main__":
    path = os.getcwd()
    print ("The current working directory is %s" % path)

    projectFolder = '/' + sys.argv[1] 


    try:
        os.mkdir(path + projectFolder)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)
        
    try:
        os.mkdir(path + projectFolder + "/project")
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)
        
    try:
        os.mkdir(path + projectFolder + "/build")
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)

    try:
        os.mkdir(path + projectFolder + "/project" + "/code")
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)
        
    try:
        os.mkdir(path + projectFolder + "/project" + "/data")
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)
        
        
        
    f = open(path + projectFolder + "/project" + "/code" + "/main.cpp","w+")

    f.write(filecontent.CPPStarter)

    f.close()


    f = open(path + projectFolder + "/shell.bat", "w+", encoding="utf-8")

    #filecontent.VSBat.encode("utf-8")

    f.write(filecontent.VSBat)

    f.close()


    f = open(path + projectFolder + "/4ed.bat", "w+", encoding="utf-8")

    #filecontent.VSBat.encode("utf-8")
    path = filefinder.find_4ed_fast()

    f.write("@echo off \nstart " + path + " -W")

    f.close()


