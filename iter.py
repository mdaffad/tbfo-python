import csv
import itertools
import DFA

A = [0, 5, 10,15]
B = [0, 5, 10,15]
C = [0, 5, 10,15]

a = [A, B, C]
data = list(itertools.product(*a))

with open('dataset.csv','wb') as out:
    csv_out=csv.writer(out)
    csv_out.writerow(['energy','hygiene','fun'])
    for row in data:
        csv_out.writerow(row)




