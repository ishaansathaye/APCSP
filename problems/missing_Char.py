def missing_char(str, n):
    return str.replace(str[n], "")

str = "abcd"
print(missing_char(str, 2))