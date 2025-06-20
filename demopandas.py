import pandas as pd
import numpy as np
import pymysql
from pymysql.cursors import DictCursor

a=[10,20,30,40]
n=np.array([10,20,30,40])

x = pd.Series(a)  #series is ordered and indexed
print(x)
for i in x:
    print(i)

y = pd.Series(n,index=["one", "two", "three", "four"])   #custom names to indices
print(y)
print(y.iloc[0])
print(y["one"])
print(type(y))


emp={"empid": [1,2,3,4], "ename": ["xyz","mno","pqr","abc"], "salary": [90000,11000,82000,34000]}
s = pd.Series(emp)
print("****************************")
print(s)        # creating series from dictionary
d = pd.DataFrame(emp, index=['one','two','three','four'])
print("--------------")
print(d)
print("---------------")
print(d.loc['two'])
print("---------------")
print(d.iloc[3])
print("=================")
print(d['salary'])
print(type(d))

connection = pymysql.connect(host= "localhost", user="root", password="root", port=3306, database="dai03", cursorclass=DictCursor)
cursor = connection.cursor()
# name = 'akki'
cursor.execute(f"SELECT * FROM Student")     # WHERE name = %s, name
result = cursor.fetchall()
df = pd.DataFrame(result)
print(df)
print("-----------------------------")
d = pd.DataFrame(result,columns=['std','name','address'])
print(d)

d.to_csv("Student.csv")