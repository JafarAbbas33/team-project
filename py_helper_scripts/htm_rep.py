#!/usr/bin/env python3

import tkinter as tk

import os
import sys
import time
import subprocess

inp = '<a'

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
            if inp in line and 'inp = ' not in line and 'url_for' not in line and 'href' in line and 'http' not in line and 'href="#"' not in line and 'www.' not in line:
                # print(line)
                # continue
                
                if 'http' not in line:
                    i = line.index('href=') + 6
                    name = line[i:]
                    temp3 = name
                    j = name.index('"')
                    temp2 = name
                    name = name[:j]
                    if name.count('/') == 1:
                        continue
                    name = name.split('/')[-1]
                    if name.startswith('#') == 1:
                        continue
                    new_text = '''<a href="/''' + name + temp2[j:temp2.index('>')+1]
                    


                    to_replace_line = line[line.index(inp):line.index('>', line.index(inp))+1]
                    # print(to_replace_line, '||', name) #, '||', fpath)
                    if True:
                    # if input(f'Convert \n{to_replace_line}\nto\n{new_text}\ny/n?: ') == 'y' or True:
                        with open(fpath, 'w') as f:
                            f.write(s.replace(to_replace_line, new_text))
                            f.close()
                    print()
            

