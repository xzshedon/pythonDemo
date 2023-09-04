#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@Time    :   2022/02/15 09:54:22
@Author  :   Xing ZiShuai 
@Version :   1.0
@Contact :   xwatson@163.com
@Description    :   None
'''


def change_string(test_list,tag_str,new_str):
    for i in range(test_list.count(tag_str)):
        ele_index = test_list.index(tag_str)
        test_list[ele_index] = new_str
    return test_list

if __name__ == "__main__":
    num_list = ["harder","lamp",88,3,33,35,55,66,77,88,3,789]
# print(num_list.count(3))  # 获得3出现的次数
# print(num_list.index(3))    # 获得3出现的index
    change_string(num_list,3,"3a")
    print(num_list)