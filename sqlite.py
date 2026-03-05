import sqlite3
import pandas as pd

#connect to sqlite datbas
conn = sqlite3.connect('ecommerce_health.db')

#load to csv's
df_comp = pd.read_csv('competitor_prices.csv')
df_int = pd.read_csv('internal_sales_us.csv')

#push to sql
df_comp.to_sql('raw_competitor_prices', conn, if_exists='replace', index=False)
df_int.to_sql('raw_internal_sales', conn, if_exists='replace', index=False)

df_master = pd.read_sql_query("SELECT * FROM v_master_pricing_analysis", conn)


print("US Database initialized successfully.")
conn.close()

