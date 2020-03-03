listOfWords = ["a", "bo", "o", "ooo"]


def wordswithoutlist(array, length):
    for i in array:
        wordLength = len(i)
        if wordLength == length:
            array.remove(i)
    return array


print(wordswithoutlist(listOfWords, 1))
