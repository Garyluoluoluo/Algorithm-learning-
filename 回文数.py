

def isPalindrome( x: int) -> bool:
    if x < 0 or x % 10 == 0:
        return False
    if x == 0:
        return True
    c = 0
    while (x!=0):
        if c == x:
            return  True
        c = c * 10 + x % 10
        if c == x:
            return  True

        x = x // 10
    return False
print(10%10)
print(isPalindrome(10))





