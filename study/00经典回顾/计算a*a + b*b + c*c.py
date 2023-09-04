#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@Time    :   2020/12/09 23:23:50
@Author  :   Xing ZiShuai 
@Version :   1.0
@Contact :   xwatson@163.com
@Desc    :   None
'''

def sum(num_list):
    total_num = 0
    for each in num_list:
        total_num += each*each 
    print(total_num)


if __name__ == "__main__":
    num_list = [1,2,3]
    sum(num_list)