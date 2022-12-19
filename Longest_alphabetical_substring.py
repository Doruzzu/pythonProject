"""
A  program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl',
then your program should print

s = 'abcdefghijklmnopqrstuvwxyz'

s = 'uifseuasgzfmwoctbqkwumex'

s = 'yfzsyesmrkswbhisso'

s = 'ftfdozesskcxmlen'


s = 'jkjjiwppwgjfzntra'

"""
s = 'abcdefghijklmnopqrstuvwxyz'

# w will contain different substrings of different lengths "
w = []

for i in range(len(s)):

    for j in range(len(s) - i):
        w = w + [s[i:i + j + 1]]

m = []

for y in w:
    s = 0
    for i in range(len(y) - 1):
        if ord(y[i + 1]) >= ord(y[i]) + 1 or ord(y[i]) == ord(y[i + 1]):
            s = s + 1
    if s == len(y) - 1:
        m = m + [y]
l = 0
inum = 0
for index, lis in enumerate(m):
    if len(lis) >= l:
        l = len(lis)
        inum = index
for i in range(len(m) - 1):
    if len(m[i]) == l:
        print("Longest substring in alphabetical order is:", m[i])
        break
