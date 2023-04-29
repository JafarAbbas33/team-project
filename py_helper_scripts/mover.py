#!/usr/bin/env python3

import tkinter as tk

import os
import sys
import time
import subprocess

inp = '<script'

match_case = True
full_res = ''
for dname, dirs, files in os.walk(os.getcwd()):
    for fname in files:
        fpath = os.path.join(dname, fname)
        if '.htm' in fpath:
            n_path = '/home/jafarabbas33/Downloads/nnn/app/app/templates/'+fname
            if input(f'{fpath}\n{n_path}\nMove? y/n: ') == 'y':
                os.rename(fpath, n_path)
            print()
