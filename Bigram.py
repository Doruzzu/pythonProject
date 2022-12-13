"""Write a Python program to form Bigrams of words in a given list of strings

A bigram or digram is a sequence of two adjacent elements from a string of tokens, which are typically letters, syllables, or words.
A bigram is an n-gram for n=2. The frequency distribution of every bigram in a string is commonly used for simple statistical analysis of text in many applications,
including in computational linguistics, cryptography, speech recognition, and so on.
Original list:
['Sum all the items in a list', 'Find the second smallest number in a list']
Bigram sequence of the said list:
[('Sum', 'all'), ('all', 'the'), ('the', 'items'), ('items', 'in'), ('in', 'a'), ('a', 'list'), ('Find', 'the'), ('the', 'second'), ('second', 'smallest'), ('smallest', 'number'), ('number', 'in'), ('in', 'a'), ('a', 'list')]"""


def bigram(list_of_strings):
    lis = []
    for string in list_of_strings:
        l = string.split(' ')
        for i in range(len(l)-1):
            lis.append((l[i],l[i+1]))
    return lis

print(bigram(['Sum all the items in a list', 'Find the second smallest number in a list']))
