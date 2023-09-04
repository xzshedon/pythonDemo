#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@Time    :   2021/11/14 23:14:03
@Author  :   Xing ZiShuai 
@Version :   1.0
@Contact :   xwatson@163.com
@Description    :   None
'''
import os

def print_dir(filepath):
    for i in os.listdir(filepath):
        path = os.path.join(filepath,i)
        if os.path.isdir(path):
            print_dir(path)
        if path.endswith(".html"):
            print(path)

if __name__ == "__main__":
    print_dir("/Users/xingzishuai/Downloads/work/python/study")