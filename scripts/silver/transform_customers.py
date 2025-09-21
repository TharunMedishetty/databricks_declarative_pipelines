 import dlt
 from pyspark.sql.functions import *


 # Creating Streaming View for Customers Transformations

 @dlt.view(
     name = 'customers_enr_view'
 )
 def customers_enr_view():
    df = spark.readStream.table('customers_stg')
    df = df.withColumn('customer_name', upper(col('customer_name')))
    return df

# Creating Empty Streaming Table for Products
dlt.create_streaming_table(
    name = 'customers_enr'
)   
# Creating auto cdc flow to UPSERT the records in silver table
dlt.create_auto_cdc_flow(
  target = "customers_enr",
  source = "customers_enr_view",    # streaming view as source since we've applied transformation in it
  keys = ["customer_id"],
  sequence_by = col("last_updated"),
  apply_as_deletes = None,
  apply_as_truncates = None,
  except_column_list = None,
  stored_as_scd_type = 1         # SCD type 1 is also known as UPSERT
)
