#!/usr/etc/env python3
import os
import sys

def path_of_executable():
    path = os.getcwd()
    path = __file__
    filename = path.split('/')[-1]
    path = path[:-len(filename)]
    return path
