def findsmalllest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest :
             smallest = arr[i]
             smallest_index = i
    return smallest_index

def selectionSort(arr) :
    newArr = []
    for i in range(len(arr)):
        smallest = findsmalllest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([3,1,5,67,2,5,1211,3,6]))

