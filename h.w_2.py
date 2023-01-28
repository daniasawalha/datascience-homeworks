# -*- coding: utf-8 -*-
"""
Created on Tue May 24 08:01:43 2022

@author: Dania
"""
import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd

#open the csv file and read it correctly ,then we make a dataframe 
with open ("D:/programing/h.w/data1.csv",) as d:
    myreader =csv.DictReader(d,delimiter=';')
    data1=[]
    #mywriter=csv.writer(d, )
    for row in myreader:
        data1.append(row)
df1=pd.DataFrame(data1)

with open ("D:/programing/h.w/data2.csv",) as d2:
    myreader2 =csv.DictReader(d2,delimiter=';')
    data2=[]
    #mywriter=csv.writer(d, )
    for row in myreader2:
        data2.append(row)
df2=pd.DataFrame(data2)
#we merage the two dataframes into a new dataframe ,and display it
df3=pd.concat([df1, df2], axis=0)
print(df3)
# all what we did put in a new file 
#EDA1=open("EDA1.csv","w")
df3.to_csv('EDA1.csv',index=False)


buy=df3["buy"]
#Display the 2nd and 4th columns from the new dataframe
print(df3[df3.columns[2]])
print(df3[df3.columns[4]])
#Find out and display information of who has (buy = Y)
print(df3[df3["buy"]=="Y" ])
#Add a new column in the new dataframe and fill it with 0 values
hh=np.zeros(len(df3))
df3["zero"]=hh
#Display the shape of the new dataframe
print(df3.shape)

#we fill the empty cells of numeric columns with null values 
df3["income"]=df3["income"].replace(to_replace ="",value=np.nan)
df3["extraIncome"]=df3["extraIncome"].replace(to_replace ="",value=np.nan)
df3["expenses"]=df3["expenses"].replace(to_replace ="",value=np.nan)


employed=df3["employed"].mode()[0]
status=df3["status"].mode()[0]
buy=df3["buy"].mode()[0]

#we convert some columns to numeric 
df3["income"]=pd.to_numeric(df3["income"])
df3["extraIncome"]=pd.to_numeric(df3["extraIncome"])
df3["expenses"]=pd.to_numeric(df3["expenses"])

#we replace the null values with mode,mean
df3["status"] = df3["status"].replace("", status )
df3["employed"]=df3["employed"].replace("",employed)
df3["income"] = (df3["income"].fillna(df3["income"].mean()))
df3["extraIncome"] = df3["extraIncome"].fillna(df3["extraIncome"].mean())
df3["expenses"] = df3["expenses"].fillna(df3["expenses"].mean())
df3["buy"] = df3["buy"].replace("", buy )

categoric=pd.concat([df3["status"],df3["employed"],df3["buy"],df3['gender']], join='outer')
cols = ["income", "extraIncome","expenses"]
# Remove the outliers
def IQR(df,cols):
    for col in cols:
        df[col]=pd.to_numeric(df[col])
        g=[]
        for i, r in df.iterrows():
            if r[col]<=40000:
                g.append(r)
        df3_9=pd.DataFrame(g)   
        #print(dfx.shape)
        #df3_9=df[df[col].any() <=40000.0].reset_index()
        print(df3_9)
        Q1=df.describe()[col]['25%']
        Q3=df.describe()[col]['75%']
        iqr=Q3-Q1

        Upper=Q3+1.5*iqr
        Lower=Q1-1.5*iqr
        
        cond=(df3_9[col] > Upper)  | ( df3_9[col] < Lower)
        lo=len(df3_9[cond])
        filtered = (df3_9[col] >= Lower) & (df3_9[col] <= Upper)
        df_out1=df3_9.loc[filtered]
        #print(df_out1)

        #draw boxplot before remove outliers
    df3.boxplot(column=[col],grid=False,figsize=(10,5))
    plt.figure(figsize=(20,10))
    #draw boxplot after remove outliers
    df_out1.boxplot(column=[col],grid=False,figsize=(10,5))
    plt.figure(figsize=(10,5))
    print(df_out1.shape)
    return df_out1
cols = ["income", "extraIncome","expenses"]
newdf3=IQR(df3,cols)
# Z score
def z_score(df,cols):
    from scipy import stats
    import numpy as np
     
    df[cols] = np.abs(stats.zscore(df[cols]))
    return df
#Normalize the numerical columns using z-score equation

#z_score(df3,"income")
#z_score(df3,"extraIncome")
#z_score(df3,"expenses")
z_score(newdf3,cols)
print(newdf3)
#Generate the dummy columns for categorical columns
e=pd.get_dummies(categoric)

print(e)

newdf3[["income","extraIncome"]].hist(bins=20,figsize=(5,3))
count=0
for row in newdf3["employed"]:
    if row=="Yes":
        count +=1
#print("the number of records which has yes is :",count)
print("the number who have yes :",count)
newdf3.to_csv('EDA2.csv',index=False)