# Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.


# rotate_left3([1, 2, 3]) → [2, 3, 1]
# rotate_left3([5, 11, 9]) → [11, 9, 5]
# rotate_left3([7, 0, 0]) → [0, 0, 7


def rotate_left3(nums):
    pos1 = nums[0]
    pos2 = nums[1]
    pos3 = nums[2]

    nums[0] = pos2
    nums[1] = pos3
    nums[2] = pos1
    return nums

print(rotate_left3([7, 0, 0]))