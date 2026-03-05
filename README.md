# eCommerce Competitive Pricing & Inventory Optimization System
Developed an end-to-end competitive pricing and inventory risk analytics system to support regional pricing strategy in an eCommerce retail environment.\
By integrating external competitor pricing data with internal sales and inventory metrics, the system enables stakeholders to evaluate regional pricing competitiveness, identify price-inelastic product categories, and detect revenue risk caused by inventory shortages or overstock.\
The resulting dashboard provides actionable insights that help guide pricing adjustments, inventory allocation, and promotional strategies.

# Business Problems & Goals
## Concerns
In competitive eCommerce markets, static national pricing strategies often fail to account for regional competitive pressures.\
The organization lacked visibility into:
- How competitor pricing varied across regions.
- How price differences affected internal sales performance.
- Where inventory shortages or excess stock created revenue risk.

Without this insight, pricing and inventory decisions were largely reactive./ 
## Primary Business Goals
The system was designed to support three operational objectives:
- **Margin Optimization**
  - Identify product categories with low price sensitivity where price premiums can be sustained.
- **Competitive Price Positioning**
  - Develop a regional Price Index to quantify how internal pricing compares to the local competitor market.
- **Inventory Risk Mitigation**
  - Surface products at risk of stock-outs or overstock to support timely supply chain and promotional decisions.

## Technical Architecture
Data Processing:
  - Python used for data ingestion and preprocessing
  - External competitor pricing dataset combined with internal transaction and inventory data
  - dbt used to model and transform data into analytical tables

# Analytics Layer
- Computed core KPI's
  - **Competitor Price Index** at **1.003** (Price Index = Company Price / Average Competitor Price)
  - **Total Revenue** at **$4.28M** (Revenue = Internal Prices * Units Sold)

## Visualization
A Tableau dashboard was developed to translate analytical outputs into decision-support insights using:
- Regional pricing heatmaps
- Price elasticity scatter plots
- Inventory risk matrices

<img width="659" height="850" alt="Screenshot 2026-03-05 at 2 40 00 PM" src="https://github.com/user-attachments/assets/4c6c7765-0372-41a7-9329-18675af64a57" />

# Key Business Insights
By analyzing the Q1 Market Health Dashboard, three critical operational insights were surfaced:
- **Premium Positioning Success:**
  - The East Region is the top revenue driver, successfully maintaining a 1.01 Price Index (a 1% premium over the market average) without sacrificing          sales volume, indicating strong regional brand equity.
  - The South region is currently the lowest performer. While it has passed the 80% of average revenue mark (Regional Revenue vs. Target), it is noticeably     shorter than the others.
- **Positive Price Elasticity in Apparel:**
  - The elasticity scatter plot revealed an upward trendline for the Lifestyle category. This counter-intuitive insight demonstrates that sales volume            actually holds steady or increases as the relative price rises, suggesting opportunity for controlled price increases.
- **Inventory Revenue-at-Risk:**
  - The Inventory Risk matrix identified critical stock-outs in the "Discount" category, representing an immediate $12K in deferred revenue, alongside a        severe overstock of the Lifestyle category in the South Region.





