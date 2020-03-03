sortedList = [1,4,5,8,10,14,15,17,20,25]
unsortedList = [1,25,4,20,5,17,8,15,10,14]
randomList = [1,3,5,7,7,5,3,1,3,5,7,1,11,9,15,13,3,3,3,3,3,3,3,3,3,5,3]


def linearSearch(list, value):
    for i in list:
        if i == value:
            return True
    return False


def position(list, value):
    for i in list:
        if i == value:
            return list.index(i)
    return 0


def removeDuplciates(list):
    unique = set()
    for i in list:
        unique.add(i)
    return (unique)


def no_duplicates_sort(list):
    return sorted(removeDuplciates(list))


print(no_duplicates_sort(randomList))
