# 9 * 9 + 7 = 88
# 98 * 9 + 6 = 888
# 987 * 9 + 5 = 8888
# 9876 * 9 + 4 = 88888
# 98765 * 9 + 3 = 888888
# 987654 * 9 + 2 = 8888888
# 9876543 * 9 + 1 = 88888888
# 98765432 * 9 + 0 = 888888888


for i in range(1,10):
    s = ''
    for j in range(9, 9-i,-1):
        s = s + str(j)
    string_s=s+ '*'+'9'+ '+' + str(j-2)
    p=int(s)*9+ j-2
    print(string_s + '=' + str(p))
