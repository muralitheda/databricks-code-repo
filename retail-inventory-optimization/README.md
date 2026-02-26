
We’ll build a **very simple Inventory Demand Prediction model**.

This is our **first time using MLlib**, we will:

* ✅ Remove advanced parts (Window, Lag, OneHotEncoder, multiple indexers)
* ✅ Keep only essential columns
* ✅ Use a simple model
* ✅ Add clear comments for every step
* ✅ Keep it beginner-friendly
* ✅ Still aligned with retail inventory optimization

---

# 🎯 Simplified Use Case

Computer manufacturer (like Dell Technologies) wants to:

> Predict next month sales quantity based only on previous month quantity.

No complex joins.
No multiple encoders.
No heavy feature engineering.

Just:

```
previous_month_quantity → predict current_month_quantity
```

---

# 📊 Expected transactions.csv

| store_id | product_id | quantity | sale_date |

---

# 🟫 STEP 1 — Load Data

```python
# Import required functions
from pyspark.sql.functions import col, month, year

# Read CSV file into DataFrame
transactions_df = (
    spark.read
        .option("header", True)        # First row contains column names
        .option("inferSchema", True)   # Automatically detect data types
        .csv("/FileStore/transactions.csv")
)

# Show sample data
transactions_df.show()
```

👉 Purpose: Load raw retail transaction data.

---

# 🟩 STEP 2 — Extract Year & Month

```python
# Create year and month columns from sale_date
transactions_df = (
    transactions_df
        .withColumn("year", year("sale_date"))
        .withColumn("month", month("sale_date"))
)

transactions_df.show()
```

👉 Purpose: Inventory prediction usually works at monthly level.

---

# 🟨 STEP 3 — Aggregate Monthly Sales

```python
from pyspark.sql.functions import sum as _sum

# Group data by store, product, year and month
monthly_sales = (
    transactions_df
        .groupBy("store_id", "product_id", "year", "month")
        .agg(
            _sum("quantity").alias("monthly_quantity")
        )
)

monthly_sales.show()
```

👉 Purpose: Get total quantity sold per month.

---

# 🟦 STEP 4 — Create Previous Month Feature

This is the only slightly advanced concept.

```python
from pyspark.sql.window import Window
from pyspark.sql.functions import lag

# Define window (group by store and product)
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

# Remove first month (because it has null previous value)
monthly_sales = monthly_sales.dropna()

monthly_sales.show()
```

👉 Purpose:
ML model needs input (feature).
We use **previous month quantity** as feature.

---

# 🎯 Define Label

We want to predict:

```
current month quantity
```

Rename column to `label` (MLlib expects this name):

```python
gold_df = monthly_sales.withColumnRenamed(
    "monthly_quantity",
    "label"
)

gold_df.show()
```

---

# 🤖 STEP 5 — MLlib (Very Simple Version)

Now comes MLlib.

We will:

* Use only 1 feature: prev_month_qty
* Use Linear Regression
* No encoding
* No pipeline complexity

---

## 1️⃣ Create Feature Vector

MLlib requires features to be in vector format.

```python
from pyspark.ml.feature import VectorAssembler

# Combine feature column into vector format
assembler = VectorAssembler(
    inputCols=["prev_month_qty"],  # Only one feature
    outputCol="features"
)

model_df = assembler.transform(gold_df)

model_df.select("prev_month_qty", "features", "label").show()
```

👉 Purpose: Convert numeric column into MLlib vector format.

---

## 2️⃣ Train/Test Split

```python
# Split data into training (80%) and testing (20%)
train_df, test_df = model_df.randomSplit([0.8, 0.2], seed=42)
```

👉 Purpose: Avoid overfitting.

---

## 3️⃣ Linear Regression Model

```python
from pyspark.ml.regression import LinearRegression

# Create regression model
lr = LinearRegression(
    featuresCol="features",  # Input column
    labelCol="label"         # Target column
)

# Train model
model = lr.fit(train_df)
```

👉 Purpose: Train simple demand prediction model.

---

## 4️⃣ Make Predictions

```python
# Apply model to test data
predictions = model.transform(test_df)

# Show prediction results
predictions.select(
    "prev_month_qty",
    "label",
    "prediction"
).show()
```

👉 Purpose: Compare actual vs predicted demand.

---

# 📊 STEP 6 — Evaluate Model

```python
from pyspark.ml.evaluation import RegressionEvaluator

# Create evaluator using RMSE
evaluator = RegressionEvaluator(
    labelCol="label",
    predictionCol="prediction",
    metricName="rmse"
)

rmse = evaluator.evaluate(predictions)

print("RMSE:", rmse)
```

👉 Purpose: Measure prediction error.

Lower RMSE = better model.

---

# 🧠 What We Just Learned

We learned:

* DataFrame transformations
* GroupBy aggregation
* Window + Lag
* Feature vector creation
* Linear Regression in MLlib
* Model evaluation

This is the **correct beginner path**.

---

# 📁 Suggested GitHub Structure (Simple Version)

```
retail-inventory-optimization/
│
├── inventory_model.py
├── sample_transactions.csv
└── README.md
```

---

# 🧑‍🏫 What we have done?

> We built a simple time-series style regression model using previous month demand to predict current demand.
> This helps supply chain teams decide optimal inventory levels.

---

# 🚀 Next step:

* Add 3-month rolling average
* Add product category
* Use RandomForestRegressor
* Add hyperparameter tuning

---
