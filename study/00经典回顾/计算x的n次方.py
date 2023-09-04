#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@Time    :   2020/12/09 23:24:20
@Author  :   Xing ZiShuai 
@Version :   1.0
@Contact :   xwatson@163.com
@Desc    :   None
'''


x = -2
n = 3

def power(x,n):
    """
    计算x的n次方
    """
    s = 1
    while n > 0:
        n = n -1
        s = s * x
    return s


if __name__ == "__main__":
    print(power(x,n))
    