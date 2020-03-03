def centered_average(nums):
    smallest = min(nums)
    largest = max(nums)
    sum = 0
    for k in nums:
        sum = sum + k
    finalSum = sum - largest - smallest
    length = len(nums) - 2
    return finalSum/length

array = [1, 1, 5, 5, 10, 8, 7]
print(centered_average(array))