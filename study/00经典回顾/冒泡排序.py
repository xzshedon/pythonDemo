#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@Time    :   2020/12/09 23:24:29
@Author  :   Xing ZiShuai 
@Version :   1.0
@Contact :   xwatson@163.com
@Desc    :   None
'''


lis0 = [687,9,45,13,2453,2,3425,5,345,123,45,678,670]
lis1 = [9]
lis2 = []

def sortfort(ele):
    """
    冒泡排序
    """
    num = len(ele)
    if num == 0:
        return "list is None"
    for i in range(num-1):
        for j in range(num-1-i):
            if ele[j] > ele[j+1]:
                ele[j], ele[j+1] = ele[j+1],ele[j]
                
    return ele


if __name__ == "__main__":
        print(sortfort(lis0))
        print(sortfort(lis1))
        print(sortfort(lis2))