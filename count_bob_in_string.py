"""Write a program that prints the number of times the string 'bob' occurs in s. For example, if

s = 'azcbobobegghakl'

s = 'boboboboowoboobobbogtxfbobboboboobobobobobobnxbobob'

s = 'bbobobvbbobobeoobobbobb'

s = 'xsruvgjjxu'

s = 'obobowboobwobobbobobobqboobomoboobboboe'

s = 'bobbxbobobobobbobobhgbobbobobooecjaboobbobobq'



"""


string_list=['boboboboowoboobobbogtxfbobboboboobobobobobobnxbobob','bbobobvbbobobeoobobbobb','xsruvgjjxu', 'bobbxbobobobobbobobhgbobbobobooecjaboobbobobq']



def count_bob_in_string(s):
    """ Counts how many times the substring "bob" appears in a string s


    """
    count=0
    for i in range(0,len(s)-1):
        if 'bob' in s[i:i+3]:
            count+=1
    return count

for elem in string_list:
    print("Number of times bob occurs is:",count_bob_in_string(elem))
