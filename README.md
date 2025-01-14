## Duplicate Removal Based on Key Attributes

### Overview:
This Python script identifies and removes duplicate records in a customer dataset by considering the combination of *Age, **Annual Income, and **Spending Score*. This process helps
clean the data, ensuring that only unique customer records are retained for analysis.

### Problem:
Datasets often contain redundant entries, which can skew analysis or model results. By removing duplicates based on key features, we can enhance data quality and ensure more reliable 
insights.

### Key Features:
- *Identify duplicates* based on a combination of Age, Annual Income, and Spending Score.
- *Remove duplicates* while keeping the first occurrence of each unique combination.
- *Save cleaned dataset* for further processing or analysis.

### Code Explanation:
The script uses *Pandas* to load the dataset, find duplicates based on selected features, and clean the dataset by removing redundant rows. Here's how it works:

```python
import pandas as pd

# Load dataset
cust = pd.read_csv('customer_data.csv')

# Remove duplicates based on Age, Annual Income, and Spending Score
cust.drop_duplicates(subset=['Age', 'Annual Income', 'Spending Score'], inplace=True)

# Save cleaned dataset
cust.to_csv('cleaned_customer_data.csv')

#print update csv file
print(cust)




