import sys 
import pandas as pd 

print('args:', sys.argv)
month = sys.argv[1]

df = pd.DataFrame({'day': [1, 2, 3], 'push_ups': [4, 5, 6]})
print(df.head())

print("month:", month)

df.to_parquet(f"output_month_{month}.parquet", index=False)