import pandas as pd
df = pd.read_excel("C:\python\coba.xlsx") 
a=[[0 for i in range(3)] for j in range (64)]
energy=df.loc[0:,"energy"]
hygiene=df.loc[0:,"hygiene"]
fun=df.loc[0:,"fun"]
print(energy[0])
