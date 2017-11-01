# -*- coding: utf-8 -*-
def binary_search(list, item ):                  #输入列表 和 需要查找的项
    low = 0
    high = len(list)-1                           #用于二份查找跟踪列表位置

    while low <= high :                          #查找到列表的最后两个数前，循环为真
        mid = (high + low)/2                     #找到跟踪位置的中间值
        guess = list[mid]                        #将中间位置的值附给暂存变量
        if guess == item :                       #若中间值与查找值相同，返回查找值
            return mid
        if guess > item :                        #若中间值大于查找值，择将跟踪位置的高位替换为中间位置减一
            high = mid - 1
        else:
            low = mid + 1                       #若中间位置小于查找值，择将跟踪位置的低位替换为中间位置加一
    return None                                 #若不存在查找值，则返回空值


test_list = [2,3,5,8,10,14,16,17,34,56,74]
item = input('input item :')
print  'location is : ',binary_search(test_list,item)