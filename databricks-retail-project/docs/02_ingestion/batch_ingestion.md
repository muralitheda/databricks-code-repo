# Batch Data Ingestion – Bronze Layer

## Objective
Ingest raw retail CSV data into Databricks and store it as **Bronze Delta tables**.

## Why Bronze Layer?
The Bronze layer represents:
- Raw, unprocessed data
- Original source format
- Traceability and reprocessing capability

No cleansing or business logic is applied at this stage.

---

## Ingestion Workflow

### Step 1: Upload Raw Files
Files are uploaded using:  
Workspace → Files → Upload


Target directory: /Workspace/Files/retail/raw/


---

### Step 2: Read CSV Files Using Spark
Spark DataFrame API is used to read raw data:

```python
spark.read \
  .option("header", True) \
  .option("inferSchema", True) \
  .csv("/Workspace/Files/retail/raw/customers.csv")


