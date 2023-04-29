#!/usr/bin/env python3

import tkinter as tk

import os
import sys
import time
import subprocess

inp = '<img'

match_case = True
full_res = ''
for dname, dirs, files in os.walk('/home/jafarabbas33/Downloads/nnn/TeamProject/app/templates'):
    for fname in files:
        fpath = os.path.join(dname, fname)

        try:
            with open(fpath) as f:
                s = f.read()
                f.close()
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
                    j = name.index('"')
                    name = name[:j]
                    name = name.split('/')[-1]
                    new_text = '''<img src="{{url_for('static', filename='images/''' + name + '''')}}">'''


                    to_replace_line = line[line.index('<'):line.index('>')+1]
                    # print(to_replace_line, '||', name) #, '||', fpath)
                    if input(f'Convert \n{to_replace_line}\nto\n{new_text}\ny/n?: ') == 'y':
                        with open(fpath, 'w') as f:
                            f.write(s.replace(to_replace_line, new_text))
                            f.close()
                    print()
            

