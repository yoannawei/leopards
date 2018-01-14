numArray = [1,2,2,3,4,5,6,7,8]
numArray2 = [1,2,3,4,5,6,6,7,8]

def find_duplicate(numArray):
    last_num = 0
    for i in range(len(numArray)):
        if numArray[i] == last_num:
            return numArray[i]
        last_num = numArray[i]

def find_duplicate2(numArray):
    first_index =0
    last_index = len(numArray) -1
    midpoint = (first_index+last_index)//2

    if numArray[midpoint] >= midpoint:
        find_duplicate2(numArray[0: midpoint])
    else:
        find_duplicate2(numArray[midpoint+1: last_index])

def find_duplicate3(numArray):
    n = len(numArray) - 1

    # get inside of a cycle

    pos_cycle = n+1
    for _ in range(n):
        pos_cycle = numArray[pos_cycle -1]






print("Duplicate in array is ", find_duplicate2(numArray))