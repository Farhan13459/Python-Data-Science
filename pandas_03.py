import pandas as pd
import numpy as np

cust=pd.read_csv("Customers.csv")
print(cust.size)
cust.drop_duplicates(subset=["Age" , "Annual Income ($)","Spending Score (1-100)"],keep="last", inplace=True)
cust.to_csv("Customers.csv")
print(cust.size)


# cust.drop_duplicates().head(20)




