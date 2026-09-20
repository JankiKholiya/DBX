# Databricks notebook source
# DBTITLE 1,Source files config
files= {"dbfs:/Volumes/etl/bronze/raw_sources/source_crm":"bronze_crm",
        "dbfs:/Volumes/etl/bronze/raw_sources/source_erp":"bronze_erp"}

# COMMAND ----------

# DBTITLE 1,Ingest to bronze tables
for file_name,table_name in files.items():
    try:
        print(f"Processing {file_name}")
        df= spark.read.csv(file_name,header=True,inferSchema=True)
        df.write.mode("overwrite").saveAsTable(f"etl.bronze.{table_name}")

    except Exception as e:
        print(f"Error occurred while igenstion {file_name}")

# COMMAND ----------

