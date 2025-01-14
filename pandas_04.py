import pandas as pd
import numpy as np

missing_value=pd.read_csv("missing_values_practice.csv")

print(missing_value.isnull().sum())

missing_value["Name"].fillna("Not specified", inplace=True)
missing_value["Math_Score"].fillna(78, inplace=True)
missing_value["Physics_Score"].fillna(100, inplace=True)
missing_value["Chemistry_Score"].fillna(59, inplace=True)
missing_value["Attendance_Percentage"].fillna(70, inplace=True)

print(missing_value)








# cleaned=cleaned_data[cleaned_data.is_unique]

# print(cleaned_data.drop_duplicates().head(10))

