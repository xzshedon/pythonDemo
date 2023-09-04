#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@Time    :   2021/11/14 22:42:43
@Author  :   Xing ZiShuai 
@Version :   1.0
@Contact :   xwatson@163.com
@Description    :   None
'''

import os

def print_dir():
    filepath = input("输入一个路径：")
    if filepath == "":
        print("请输入正确的路径")
    else:
        for i in os.listdir(filepath):
            print(os.path.join(filepath,i))

if __name__ == "__main__":
    print_dir()