End-to-end guide:

> ✅ Databricks Community Edition. 
> ✅ Simple Inventory Optimization (Regression). 
> ✅ Clean MLlib (no unnecessary complexity). 
> ✅ GitHub integration. 
> ✅ Portfolio-ready structure. 

Platform used:

* Databricks
* GitHub

---

# 🎯 PROJECT OVERVIEW

## 🏢 Business Problem

A computer retail company (like Dell Technologies) wants to:

> Predict current month demand using previous month sales
> → So inventory can be optimized.

We will build:

```text
CSV → Feature Engineering → ML Model → Predictions → GitHub
```

---

# 🧩 PART 1 — Setup in Databricks

---

## ✅ Step 1 — Create Cluster

1. Go to **Compute**
2. Click **Create Cluster**
3. Name: `inventory-ml-cluster`
4. Keep default settings
5. Click **Create**

Wait until status = Running.

---

## ✅ Step 2 — Create Notebook

1. Workspace → Create → Notebook
2. Name: `inventory_model`
3. Language: Python
4. Attach cluster

---

## ✅ Step 3 — Upload CSV

Left panel → Data → Upload file

Upload: `transactions.csv`

Note the path:

```
dbfs:/FileStore/tables/transactions.csv
```

---

# 🧠 PART 2 — Build ML Project (Simple & Clean)

Copy this entire code into your notebook (clean version with comments):

---

```python
# ============================================================
# STEP 1 — Load Data
# ============================================================

from pyspark.sql.functions import col, year, month

# Read transaction CSV file
transactions_df = (
    spark.read
        .option("header", True)        # First row as column names
        .option("inferSchema", True)   # Auto detect data types
        .csv("dbfs:/FileStore/tables/transactions.csv")
)

display(transactions_df)
```

---

```python
# ============================================================
# STEP 2 — Extract Year & Month
# ============================================================

# Inventory forecasting is done monthly
transactions_df = (
    transactions_df
        .withColumn("year", year("sale_date"))
        .withColumn("month", month("sale_date"))
)

display(transactions_df)
```

---

```python
# ============================================================
# STEP 3 — Aggregate Monthly Sales
# ============================================================

from pyspark.sql.functions import sum as _sum

# Calculate total quantity per store per product per month
monthly_sales = (
    transactions_df
        .groupBy("store_id", "product_id", "year", "month")
        .agg(
            _sum("quantity").alias("monthly_quantity")
        )
)

display(monthly_sales)
```

---

```python
# ============================================================
# STEP 4 — Create Previous Month Feature
# ============================================================

from pyspark.sql.window import Window
from pyspark.sql.functions import lag

# Define window per store & product
window_spec = (
    Window
        .partitionBy("store_id", "product_id")
        .orderBy("year", "month")
)

# Create previous month quantity column
monthly_sales = monthly_sales.withColumn(
    "prev_month_qty",
    lag("monthly_quantity", 1).over(window_spec)
)

# Remove null rows (first month has no previous month)
monthly_sales = monthly_sales.dropna()

display(monthly_sales)
```

---

```python
# ============================================================
# STEP 5 — Prepare ML Dataset
# ============================================================

# Rename monthly_quantity to 'label'
# MLlib expects target column to be named 'label'
gold_df = monthly_sales.withColumnRenamed(
    "monthly_quantity",
    "label"
)

display(gold_df)
```

---

```python
# ============================================================
# STEP 6 — Convert Feature to Vector
# ============================================================

from pyspark.ml.feature import VectorAssembler

# MLlib requires features in vector format
assembler = VectorAssembler(
    inputCols=["prev_month_qty"],   # Our only feature
    outputCol="features"
)

model_df = assembler.transform(gold_df)

display(model_df.select("prev_month_qty", "features", "label"))
```

---

```python
# ============================================================
# STEP 7 — Train/Test Split
# ============================================================

# Split data into training (80%) and testing (20%)
train_df, test_df = model_df.randomSplit([0.8, 0.2], seed=42)

print("Training Rows:", train_df.count())
print("Testing Rows:", test_df.count())
```

---

```python
# ============================================================
# STEP 8 — Train Linear Regression Model
# ============================================================

from pyspark.ml.regression import LinearRegression

# Create Linear Regression model
lr = LinearRegression(
    featuresCol="features",
    labelCol="label"
)

# Train the model
model = lr.fit(train_df)
```

---

```python
# ============================================================
# STEP 9 — Make Predictions
# ============================================================

predictions = model.transform(test_df)

display(predictions.select(
    "prev_month_qty",
    "label",
    "prediction"
))
```

---

```python
# ============================================================
# STEP 10 — Evaluate Model
# ============================================================

from pyspark.ml.evaluation import RegressionEvaluator

# Evaluate using RMSE
evaluator = RegressionEvaluator(
    labelCol="label",
    predictionCol="prediction",
    metricName="rmse"
)

rmse = evaluator.evaluate(predictions)

print("RMSE:", rmse)
```

---

# 🎉 Congratulations

You built:

✔ Inventory Forecasting Model
✔ Feature Engineering
✔ Regression Model
✔ Model Evaluation

---

# 🧩 PART 3 — Connect to GitHub

---

## ✅ Step 1 — Create GitHub Repo

In GitHub:

Create repo:

```
retail-inventory-optimization-ml
```

Make it Public.

---

## ✅ Step 2 — Connect GitHub to Databricks

Databricks → User Settings → Git Integration

Generate GitHub Personal Access Token

Paste token into Databricks.

---

## ✅ Step 3 — Clone Repo

Workspace → Repos → Add Repo

Paste GitHub repo URL.

---

## ✅ Step 4 — Move Notebook to Repo

Drag notebook into repo folder
OR create new notebook inside repo folder.

---

## ✅ Step 5 — Export as Python File

File → Export → Source File

Save as:

```
inventory_model.py
```

Commit & Push.

---

# 📁 Final GitHub Structure

```
retail-inventory-optimization-ml/
│
├── inventory_model.py
├── sample_transactions.csv
├── README.md
```

---

# 📝 What to Write in README

Include:

* Business Problem
* Architecture
* Tech Stack
* Steps
* RMSE result

---

# 🚀 Line

> Built an end-to-end Inventory Optimization model using PySpark MLlib on Databricks and version-controlled using GitHub.

---

# 🎯 What We Learned

* Spark transformations
* Window functions
* Feature engineering
* MLlib basics
* Regression model
* Model evaluation
* GitHub integration

---

