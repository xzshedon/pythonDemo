#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@Time    :   2021/11/14 23:04:47
@Author  :   Xing ZiShuai 
@Version :   1.0
@Contact :   xwatson@163.com
@Description    :   None
'''
import os

def show_dir(filepath):
    for i in os.listdir(filepath):
        path = (os.path.join(filepath,i))
        if os.path.isdir(path):
            show_dir(path)
        else:
            print(path)

if __name__ == "__main__":
    show_dir("/Users/xingzishuai/Downloads/work/python/study")