# Retail Data Model

## Core Entities
- Customers
- Products
- Orders
- Order Items
- Stores

## Fact Tables
- **fact_orders:** Order-level transactions
- **fact_order_items:** Product-level sales

## Dimension Tables
- **dim_customers:** Customer details
- **dim_products:** Product details
- **dim_stores:** Store details

## Schema Design
The project follows a **Star Schema** design:
- Fact tables at the center
- Dimension tables connected via keys

## Usage
This data model will be implemented using:
- Delta Lake
- Medallion Architecture (Bronze, Silver, Gold)
