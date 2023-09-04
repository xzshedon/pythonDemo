#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@Time    :   2021/01/14 23:24:20
@Author  :   Xing ZiShuai 
@Version :   1.0
@Contact :   xwatson@163.com
@Desc    :   运用递归的思想
'''

def factorial(n):
    if n ==1:
        return 1
    return n*factorial(n-1)


if __name__ == "__main__":
    print(factorial(3))
