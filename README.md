# eCommerce Competitive Pricing & Inventory Optimization System
Developed an end-to-end competitive pricing and inventory risk analytics system to support regional pricing strategy in an eCommerce retail environment.\
By integrating external competitor pricing data with internal sales and inventory metrics, the system enables stakeholders to evaluate regional pricing competitiveness, identify price-inelastic product categories, and detect revenue risk caused by inventory shortages or overstock.\
The resulting dashboard provides actionable insights that help guide pricing adjustments, inventory allocation, and promotional strategies.

# Business Problems & Goals
In competitive eCommerce markets, static national pricing strategies often fail to account for regional competitive pressures.\
The organization lacked visibility into:
- How competitor pricing varied across regions.
- How price differences affected internal sales performance.
- Where inventory shortages or excess stock created revenue risk.

Without this insight, pricing and inventory decisions were largely reactive./ 
## Primary Business Goals
The system was designed to support three operational objectives:
- Margin Optimization
  - Identify product categories with low price sensitivity where price premiums can be sustained.
- Competitive Price Positioning
  - Develop a regional Price Index to quantify how internal pricing compares to the local competitor market.
- Inventory Risk Mitigation
  - Surface products at risk of stock-outs or overstock to support timely supply chain and promotional decisions.

# Technical Architecture
Data Processing:
  - Python used for data ingestion and preprocessing
  - External competitor pricing dataset combined with internal transaction and inventory data
  - dbt used to model and transform data into analytical tables

## Analytics Layer
- Computed core KPI's
  - Competitor Price Index (Price Index = Company Price / Average Competitor Price)
  - 

Visualization

A Tableau dashboard was developed to translate analytical outputs into decision-support insights using:

Regional pricing heatmaps

Price elasticity scatter plots

Inventory risk matrices
