import pandas as pd
import csv
df = pd.read_csv("dataset.csv") 
a=[(0,0,0) for j in range (64)]
energy=df.loc[0:,"energy"]
hygiene=df.loc[0:,"hygiene"]
fun=df.loc[0:,"fun"]
for i in range (64):
    if (fun[i]+10<=15) and (energy[i]-5>=0):
        fun[i]+=10
        energy[i]-=5
    a[i]=(energy[i],hygiene[i],fun[i])
    print(a[i])
with open('Mendengarkan.csv','wb') as out:
    csv_out=csv.writer(out)
    csv_out.writerow(['energy','hygiene','fun'])
    for i in range (64):
        csv_out.writerow(a[i]) 


