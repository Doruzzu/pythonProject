# Print all
# 1 * 8 + 1 = 9
# 12 * 8 + 2 = 98
# 123 * 8 + 3 = 987
# 1234 * 8 + 4 = 9876
# 12345 * 8 + 5 = 98765
# 123456 * 8 + 6 = 987654
# 1234567 * 8 + 7 = 9876543
# 12345678 * 8 + 8 = 98765432
# 123456789 * 8 + 9 = 987654321

for i in range(1, 10):
    first_s = ''
    for j in range(1, i + 1):
        first_s = first_s + str(j)
    s = first_s + "*" + '8' + "+"+ str(j)
    p = int(first_s) * 8 + int(j)
    print(s + "="+str(p))
