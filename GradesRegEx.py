import re
def grades():
    with open ("grades.txt", "r") as file:
        grades = file.read()
    pattern=r'([A-Z]{1}[a-z]+\s[A-Z]{1}[a-z]+)(:\sB)'
    grades_list=grades.split('\n')
    list_names=[re.match(pattern,word) for word in grades_list]
    student_list=[elem.group(1) for elem in list_names if elem!=None]
    return student_list

print(grades())