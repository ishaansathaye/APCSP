# Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.


# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

def count_evens(nums):
    counter = 0
    for x in nums:
        if x % 2 == 0:
            counter = counter + 1
    return counter

def count_evens2(nums):
    counter = 0
    length = len(nums)
    for x in range(0, length):
        if nums[x] % 2 == 0:
            counter = counter + 1
    return counter

def count_evens3(nums):
    num = 0
    counter = 0
    length = len(nums)
    while num < length:
        if nums[num] % 2 == 0:
            counter+= 1
        num = num + 1
    return counter


print(count_evens3([2, 2, 2, 3, 4]))