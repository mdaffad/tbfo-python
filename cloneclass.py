import pandas as pd
from DFA import Makan,__init__
df = pd.read_csv("dataset.csv") 
a=[[0 for i in range(3)] for j in range (64)]
energy=df.loc[0:,"energy"]
hygiene=df.loc[0:,"hygiene"]
fun=df.loc[0:,"fun"]
print(energy[0])

print("test")
my_objects = []
for i in range(64):
    my_objects.append(DFA(energy[i],hygiene[i],fun[i]))
    print(my_objects[i].energy)
