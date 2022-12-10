"""[0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]] """



def flatten_list(L):
    l=[]

    def helper_list(lis: object) -> object:
        l=[]
        for i in lis:
            l.append(i)
        return l

    for i in L :
        if type(i)== list:
           l.extend(helper_list(i))
        else:
            l.append(i)
    return l
print(flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]))




