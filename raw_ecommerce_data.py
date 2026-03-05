import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime, timedelta
import urllib3

# Setup
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
regions = ['West', 'East', 'Central', 'South']
category_map = {'Hoodie': 'Apparel', 'Jeans': 'Apparel', 'Tee': 'Apparel', 'Shoes': 'Footwear'}

# Since data on ecommerce site is limited, I added more data to from differet 'regions', 'category', and some
# 'dates' to simualte real ecommerce data
# DATA is RANDOMIZED (within reason) for better insights and value
 
def generate_dual_history_pipeline():
    # 1. SCRAPE THE "SEED" DATA
    headers = {"User-Agent": "Mozilla/5.0"}
    url = "https://www.scrapingcourse.com/ecommerce/"
    response = requests.get(url, headers=headers, verify=False)    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    seeds = []
    for item in soup.select('li.product'):
        name = item.select_one('h2').text.strip()
        price = float(item.select_one('span.amount').text.strip().replace('$', '').replace(',', ''))
        cat = next((v for k, v in category_map.items() if k in name), 'Lifestyle')
        seeds.append({"name": name, "price": price, "category": cat})

    competitor_history = []
    internal_history = []

    # 2. GENERATE 30 DAYS OF UNIQUE DATA FOR BOTH
    for i in range(30):
        date = (datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d')
        for region in regions:
            for prod in seeds:
                # --- Competitor Table Logic ---
                # Prices fluctuate slightly by day/region to look real
                c_price = round(prod['price'] + np.random.uniform(-2, 2), 2)
                competitor_history.append({
                    "date": date,
                    "region": region,
                    "category": prod['category'],
                    "product_name": prod['name'],
                    "competitor_price": max(c_price, 5.0)
                })

                # --- Internal Table Logic ---
                # We randomize our own price and performance
                i_price = round(prod['price'] + np.random.uniform(-5, 5), 2)
                internal_history.append({
                    "date": date,
                    "region": region,
                    "category": prod['category'],
                    "product_name": prod['name'], # This is our Join Key
                    "internal_price": max(i_price, 5.0),  #usually hidden fields in compeitor data
                    "units_sold": np.random.randint(5, 100),
                    "inventory_level": np.random.randint(0, 200)
                })

    # 3. SAVE TO SQLITE AS SEPARATE TABLES
    conn = sqlite3.connect('ecommerce_health_us.db')
    pd.DataFrame(competitor_history).to_sql('raw_competitor_data', conn, if_exists='replace', index=False)
    pd.DataFrame(internal_history).to_sql('raw_internal_sales', conn, if_exists='replace', index=False)
    conn.close()
    
    print(f"Success! Generated {len(competitor_history)} Competitor rows and {len(internal_history)} Internal rows.")

if __name__ == "__main__":
    generate_dual_history_pipeline()