#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@Time    :   2022/01/06 00:07:55
@Author  :   Xing ZiShuai 
@Version :   1.0
@Contact :   xwatson@163.com
@Description    :   None
'''

def dict_inversion(test_dict):
    new_dict = {}
    for key,value in test_dict.items():
        new_dict[value] = key
    return new_dict

def dict_inv(test_dict):
    print({y:x for x,y in test_dict.items()})

if __name__ == "__main__":
    test_dict = {"one":1,"two":2,"three":3}
    print(dict_inversion(test_dict))
    dict_inv(test_dict)