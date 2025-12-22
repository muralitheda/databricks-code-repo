# Data Sources – Retail Project

## Source Type
- Batch data
- CSV files
- Uploaded manually for learning purposes

## Retail Datasets
The following datasets are used in this project:
- customers.csv
- products.csv
- stores.csv
- orders.csv
- order_items.csv

## Upload Method (Databricks Free Edition)
In Databricks Free Edition:
- Public DBFS locations like `/FileStore` are disabled
- Files are uploaded using **Workspace → Files**

## Storage Location
All raw files are stored in:  
/Workspace/Files/retail/raw/

## Notes
- This approach is recommended for learning and PoCs
- In production, data typically comes from cloud storage like:
  - AWS S3
  - Azure Data Lake
  - Google Cloud Storage