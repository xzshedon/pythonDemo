from typing import Optional

'''
给你两个非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0开头。
来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

例：
2 4 3
5 6 4
————————
7 0 8

即：342 + 465 = 807

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 为了执行算法，需要书写创建单链表的初始化部分 （非解题代码）
class LinkList:
    def __init__(self):
        self.head = None

    def init_list(self, data):
        # 创建头结点,入参data为list
        self.head = ListNode(data[0])
        r = self.head
        p = self.head
        # 逐个为data内的数据创建结点，建立单链表
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return r

    def print_list(self, head):
        if head == None: return
        node = head
        while node != None:
            print(node.val, end=" ")
            node = node.next
        print()  # 添加换行，增加可读性


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dumpy = ListNode()    # 哨兵节点
        carry = 0   # 进位
        while l1 or l2 or carry:    # 有一个不是空节点，或者还有进位，就继续迭代
            carry += (l1.val if l1 else 0) + (l2.val if l2 else 0)  # 计算节点值+进位
            cur.next = ListNode(carry % 10)     # 每个节点保存个位数
            carry //= 10        # 新的进位值
            cur = cur.next      # 光标指向下一个节点
            if l1: l1 = l1.next     # l1下一个节点
            if l2: l2 = l2.next     # l2下一个节点
        return dumpy.next       # 初始节点的下一个节点，是整个链表的头节点


if __name__ == '__main__':
    l = LinkList()
    data1 = [2, 4, 3]
    data2 = [5, 6, 4]
    l1 = l.init_list(data1)
    l2 = l.init_list(data2)
    l.print_list(l1)
    l.print_list(l2)

    l3 = Solution().addTwoNumbers(l1, l2)
    l.print_list(l3)

    '''
    思考：
    1、链表不是直接生成，再去赋值，而是创建一个个节点，并通过next关联起来的
    2、可以先创建空节点，通过循环将l1,l2的header包进去，减少代码重复，最后取空节点的next，就能得到目标链表的header
    3、cur = dumpy = ListNode() 浅拷贝，实际操作的同一个链表，cur用作光标指向；通过dumpy.next找到目标链表的header
    '''
