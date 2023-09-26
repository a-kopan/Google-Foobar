#check if the list is decreasing
def is_strictly_decreasing(l: list) -> bool:
    for ind in range(1,len(l)):
        if l[ind]>=l[ind-1]:
            return False
    return True

#copy the array and replace element at given index
def copy_and_replace(old_arr: list, index: int, value: int):
    new_arr = old_arr.copy()
    new_arr.pop(index)
    new_arr.insert(index,value)
    return new_arr

#check if every digit in the array differs only by one with the neighbours
def differs_by_one(arr: list) -> bool:
    for index in range(1,len(arr)):
        if abs(arr[index]-arr[index-1])!=1:
            return False
    return True

#find all the numbers that can be determined based on the previous results
def find_based_on_previous(prev_arr: list) -> list:
    current = []
    for arr in prev_arr:
        for ind in range(len(arr)):
            new_num = arr[ind]+1
            new_arr = copy_and_replace(arr,ind,new_num)
            if is_strictly_decreasing(new_arr) and not (new_arr in current):
                current.append(new_arr)
        if is_strictly_decreasing(arr) and differs_by_one(arr) and arr[-1]!=1:
            current.append(arr+[1])
    return current

#solution
def solution(n):
    combinations = dict()
    combinations[3] = [[2,1]]
    for i in range(4,n+1):
        combinations[i] = find_based_on_previous(combinations[i-1])
    return combinations[n], len(combinations[n])

"""
3:  21
4:  31
5:  41, 32
6:  51, 42, 321
7:  61, 52, 43, 421
8:  71, 62, 53, 521, 431
9:  81, 72, 63, 54, 621, 531, 432
10: 91, 82, 73, 64, 721, 631, 541, 532, 4321
11: 9|2, 8|3, 7|4, 6|5, 8|2|1, 7|3|1, 6|4|1, 6|3|2, 5|4|2, 5|3|2|1, 10|1
"""

print(solution(50))