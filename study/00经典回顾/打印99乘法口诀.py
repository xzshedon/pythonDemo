#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@Time    :   2022/02/15 09:40:04
@Author  :   Xing ZiShuai 
@Version :   1.0
@Contact :   xwatson@163.com
@Description    :   None
'''

def print_99():
    for i in range(10):
        for j in range(1,i+1):
            print('{}x{}={}\t'.format(j,i,i*j),end='')

if __name__ == "__main__":
    print_99()