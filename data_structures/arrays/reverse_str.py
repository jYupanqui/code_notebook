"""
Reverse a given string
"""


# easy python way
def reverse(string):
    return string[::-1]


# Normal
def reverse2(string):
    new_st = [string[i] for i in range(len(string) - 1, -1, -1)]
    return ''.join(new_st)


def reverse3(string):
    return ''.join(reversed(list(string)))


print(reverse3("HI my name is josue"))
