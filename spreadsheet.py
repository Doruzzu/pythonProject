import csv

f=open("housing.csv",encoding='latin-1')
csvreader=csv.reader(f)

header=[]
header=next(csvreader)


rows=[]
for row in csvreader:
    rows.append(row)

f.close()

answear: str=input("Enter command:")

while answear != 'exit':

