# Given an array of ints, return a new array length 2 containing the first and last elements from the original array.
# The original array will be length 1 or more.


# make_ends([1, 2, 3]) → [1, 3]
# make_ends([1, 2, 3, 4]) → [1, 4]
# make_ends([7, 4, 6, 2]) → [7, 2]

def make_ends(nums):
    first = nums[0]
    length = len(nums)
    last = nums[length-1]
    newArray = []
    newArray.append(first)
    newArray.append(last)
    return newArray

print(make_ends([1, 2, 3]))