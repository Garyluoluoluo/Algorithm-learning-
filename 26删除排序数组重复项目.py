


def removeDuplicates(nums: List[int]) -> int:
    i = 0
    for j in nums[1:] :
        if j != nums[i]:
            nums[i +1] = j
            i+=1
    return nums
