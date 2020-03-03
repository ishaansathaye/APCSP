# Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all
# the other elements to be that value. Return the changed array.


# max_end3([1, 2, 3]) → [3, 3, 3]
# max_end3([11, 5, 9]) → [11, 11, 11]
# max_end3([2, 11, 3]) → [3, 3, 3]

def max_end3(nums):
    first = nums[0]
    last = nums[2]
    if first >= last:
        for i in range(0, 3):
            nums[i] = first
    elif last >= first:
        for i in range(0, 3):
            nums[i] = last
    return nums


print(max_end3([11, 3, 3]))
