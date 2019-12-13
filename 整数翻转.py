def reverse(x: int) -> int:
    flag = 1
    if x < 0:
        x = x * -1
        flag = -1
    tempx = str(x)
    tempx2 = ""
    for i in tempx:
        tempx2 = i + tempx2
    result = int(tempx2) * flag
    if result > 2 ** 31 - 1 or result < -(2 ** 31):
        return 0
    return result


reverse(321)