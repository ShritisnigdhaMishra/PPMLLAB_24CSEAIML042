#WAP to to read CSV and JSON files. 
import pandas as pd 
df_csv = pd.read_csv('D:\PPMLLAB_24CSEAIML042\Experiment no-11\sample.csv')  # Replace 'sample.csv' with your file path 
print("DataFrame from CSV:") 
print(df_csv) 
 
# Reading a JSON file 
df_json = pd.read_json('D:\PPMLLAB_24CSEAIML042\Experiment no-11\sample.json', orient='records')  # Replace 'sample.json' with your file path 
print("\nDataFrame from JSON:") 
print(df_json)