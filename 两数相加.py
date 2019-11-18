# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
# #
# # 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# #
# # 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# #
# # 示例：
# #
# # 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# # 输出：7 -> 0 -> 8
# # 原因：342 + 465 = 807
# #
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#第一次解题，链表定义见/数据结构知识/链表.md

class Solution:
    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(0)
        if (l1.val + l2.val) < 10:
            l3.val = l1.val + l2.val
            if l1.next == None:
                l3.next = l2.next
            elif l2.next == None:
                l3.next = l1.next
            else:
                l3.next = Solution.addTwoNumbers(l1.next, l2.next)
        if (l1.val + l2.val) > 9:
            l3.val = l1.val + l2.val - 10
            if l1.next == None:
                l3.next = l2.next

            elif l2.next == None:
                l3.next = l1.next

            else:
                l3.next = Solution.addTwoNumbers(l1.next, l2.next)
            if l3.next is not None:
                l3.next = Solution.addTwoNumbers(l3.next,ListNode(1))
            else:
                l3.next = ListNode(1)
        return l3

    def addTwoNumbers2(l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(0)
        if l1  == None:
            l1 = ListNode(0)
        if l2 == None:
            l2 = ListNode(0)
        if l1.next == None:
            l3.next = l2.next
        elif l2.next == None:
            l3.next = l1.next
        else:
            l3.next = Solution.addTwoNumbers2(l1.next,l2.next)
        if l1.val+l2.val<10 :
            l3.val = l1.val+l2.val
        else:
            l3.val = l1.val + l2.val - 10
            l3.next = Solution.addTwoNumbers2(l3.next,ListNode(1))
        return l3


l1 = ListNode(0)
l2 = ListNode(7)
l2.next=ListNode(3)

result =Solution
ls = result.addTwoNumbers(l1=l1,l2=l2)
print(ls)

