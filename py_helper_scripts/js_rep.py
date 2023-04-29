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

        try:
            with open(fpath) as f:
                s = f.read()
        except UnicodeDecodeError:
            s = ""
            pass
        # Ignore case
        # if match_case: inp if match_case else inp.lower()
        # if inp.lower() in s.lower():
        inp = inp if match_case else inp.lower()
        s = s if match_case else s.lower()

        for line in s.splitlines():
            if inp in line and 'inp = ' not in line and 'url_for' not in line:
                if 'http' not in line:
                    i = line.index('src=') + 5
                    name = line[i:]
##                    print('::', name, line)
                    j = name.index('"')
                    name = name[:j]
##                    print('::', name)
                    name = name.split('/')[-1]
##                    print('::', name)
                    new_text = '''<script src="{{url_for('static', filename='scripts/''' + name + '''')}}"></script>'''


                    to_replace_line = line[line.index('<'):line.index('>')+1]
                    # print(to_replace_line, '||', name) #, '||', fpath)
                    if input(f'Convert \n{to_replace_line}\nto\n{new_text}\ny/n?: ') == 'y':
                        with open(fpath, 'w') as f:
                            f.write(s.replace(to_replace_line, new_text))
                    print()
            

