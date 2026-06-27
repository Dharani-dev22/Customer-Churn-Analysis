import pandas as pd

df = pd.read_csv('raw_customer_data.csv')
df = df.drop_duplicates()
df['Gender'] = df['Gender'].replace({'F': 'Female'})

 
average_charge = df['Monthly_Charges'].mean()
df['Monthly_Charges'] = df['Monthly_Charges'].fillna(average_charge)

 
median_tenure = df['Tenure_Months'].median()
df['Tenure_Months'] = df['Tenure_Months'].fillna(median_tenure)
 

df.to_csv('cleaned_customer_data.csv', index=False)
print("Data successfully imputed, cleaned, and saved!")