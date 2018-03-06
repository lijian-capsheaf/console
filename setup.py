#!/usr/bin/python
# -*- coding: utf-8 -*-

# setup console

import os
import sys
from glob import glob as glob

MAINDIR = os.path.split(os.path.realpath(__file__))[0] + "/" + "console-shell-1.0.0-1/"
TYPE = ["dir", "file"]
MODE = ["hd","hf", "f", "d"]


# main console
def setup():
    do(MAINDIR)



# do setup
def do(path = ""):
    dirs = []
    files = []
    dirs,files = getfile(path, TYPE)
    if files != []:
        cpfile(files)
    if dirs != []:
        for dir in dirs:
            if not os.path.exists(changefilename(dir)):
                os.makedirs(changefilename(dir))
                
            do(dir)
    return 


# get list about dir and file 
def getfile(path = "",type = []):
    result = []
    dir = []
    file = []

    if path != "":
        if "dir" in type:
            dir = findfile(path, ["hd", "d"])   
        if "file" in type:
            file = findfile(path, ["hf", "f"])
    return dir ,file


# find file from path
def findfile(path = "", mode = []):
    result = list()   
    hd = list()
    hf = list()
    d = list()
    f = list()

    if path != "":
        if "hd" in mode:
            hd = glob(path + ".*/")
        if "hf" in mode:
            hf = list(set(glob(path + ".*")) - set(dealdirname(glob(path + ".*/"))))
        if "f" in mode:
            f= list(set(glob(path + "*")) - set(dealdirname(glob(path + "*/"))))
        if "d" in mode:
            d= glob(path + "*/")
    result.extend(hd)
    result.extend(hf)
    result.extend(d)
    result.extend(f)
    return result


# cut '/'
def dealdirname(dirs = []):
    newdirs = []
    for dir in dirs:
        dir = dir[:-1]
        newdirs.append(dir)
    return newdirs


# copy file 
def cpfile(filenames = []):
    if filenames != []:
        for filename in filenames:
            cmd = "cp -v " + filename + " " + changefilename(filename)
            os.system(cmd)

# change a new file nam
def changefilename(oldfilename = ""):
    if oldfilename != "":
        if oldfilename.startswith(MAINDIR):
            return oldfilename.split(MAINDIR)[1]
        
# error
def error(str = ""):
    print str


setup()
