#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@Time    :   2021/09/09 00:54:25
@Author  :   Xing ZiShuai
@Version :   1.0
@Contact :   xwatson@163.com
@Description    :   None
'''

'''
 洗牌问题：有个长度为2n的数组{a1,a2,a3,…,an,b1,b2,b3,…,bn}，
 希望排序后{a1,b1,a2,b2,….,an,bn}，请考虑有无时间复杂度o(n)，空间复杂度0(1)的解法。
'''
import random

def perfect_shuffle(my_list):
    if len(my_list) % 2 != 0 :
        return "目标list不符合要求"
    ''' python中除法/返回的是浮点数，//除法会去掉小数，返回比实际数小的整数'''
    n = len(my_list)//2      
    new_list =[]
    for i in range(int(n)):
        new_list.append(my_list[i])
        new_list.append(my_list[n+i])
    return new_list

def knuth(tag_list):
    i = len(tag_list)-1
    while i >= 0:
        temp = random.randint(0,i)
        tag_list[i], tag_list[temp] = tag_list[temp],tag_list[i]
        i = i -1 
    return tag_list


if __name__ == "__main__":
    test_1 = [1,2,3,4,5,6,7,8,9,10,21,22,23,24,25,26,27,28,29,30]
    print(perfect_shuffle(test_1))

    test_2 = [1,2,3,4,5,6,7,8,9,10,"a","b","c","d","e","f","g","h"]
    print(knuth(test_2))
