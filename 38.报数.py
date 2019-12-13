

def countAndSay(n: int) -> str:
    if n == 1:
        return "1"
    else:
        str1 = countAndSay(n - 1)
        nums = str1[0]
        count = 1
        person = ""
        for i in str1[1:]:
            if i == nums:
                count += 1
            else:
                person += str(count) + nums
                nums = i
                count = 1
        return person
countAndSay(2)