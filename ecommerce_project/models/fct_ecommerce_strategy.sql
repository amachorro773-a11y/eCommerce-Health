SELECT 
    i.date,
    i.region,
    c.category, -- <--- This "enriches" your sales data
    i.product_name,
    i.internal_price,
    c.competitor_price,
    i.units_sold,
    i.inventory_level,
    ROUND(i.internal_price * i.units_sold) AS revenue,
    ROUND(i.internal_price / c.competitor_price, 2) AS price_index
FROM raw_internal_sales i
LEFT JOIN raw_competitor_data c 
    ON i.product_name = c.product_name 
    AND i.date = c.date 
    AND i.region = c.region