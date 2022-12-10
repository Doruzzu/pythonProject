'''Program to pack consecutive duplicates of a given list elements into sublists
     Original list:
     [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
     After packing consecutive duplicates of the said list elements into sublists:
     [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]'''


def pack_consecutives(L):
    lis=[]
    l=[L[0]]
    i=0
    for i in range(1,len(L)):

        if L[i] in l:
            l.append(L[i])

        elif L[i] not in l:
            lis.extend([l])
            l = [L[i]]
    lis.extend([l])

    return lis






print(pack_consecutives([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]))



