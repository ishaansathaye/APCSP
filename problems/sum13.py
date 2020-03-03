# Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky,
# so it does not count and numbers that come immediately after a 13 also do not count.


# sum13([1, 2, 2, 1]) → 6
# sum13([1, 1]) → 2
# sum13([1, 2, 2, 1, 13]) → 6

def sum13(nums):
    sumOfArray = 0
    length = len(nums)
    print(length)
    if length == 0:
        return sumOfArray
    for x in range(0, length):
        if nums[x] == 13:
            sumOfArray = sumOfArray
        elif (nums[x-1] == 13) and (x != 0):
            sumOfArray
        else:
            sumOfArray = sumOfArray + nums[x]
    return sumOfArray


print(sum13([5, 13, 2]))

