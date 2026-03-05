import sqlite3
import pandas as pd

conn = sqlite3.connect('ecommerce_health_us.db')

df = pd.read_sql_query("SELECT * FROM fct_ecommerce_strategy", conn)

df.to_csv('clean_data.csv', index=False)
conn.close()

print("CSV exported")