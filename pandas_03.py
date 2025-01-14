import pandas as pd
import numpy as np

cust=pd.read_csv("Customers.csv")

print(cust.drop_duplicates(subset=["Age" , "Annual Income ($)","Spending Score (1-100)"],keep="last").tail(10))

print(cust.drop_duplicates(subset=["Profession","Family Size"]).head(20))

print(cust.drop_duplicates(subset=["Profession"]).head(20))



# cust.drop_duplicates().head(20)




