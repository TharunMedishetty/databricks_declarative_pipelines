import dlt
from pyspark.sql.functions import *

# Creating Streaming View for Sales transformations
@dlt.view(
    name = 'sales_enr_view'
)
def sales_stg_trnfm():
    df = spark.readStream.table('sales_stg')
    df = df.withColumn('total_amount', col('quantity')*col('amount'))
    return df


# Creating Empty Streaming Table for Sales
dlt.create_streaming_table(
    name = 'sales_enr'
)   
# Creating auto cdc flow to UPSERT the records in silver table
dlt.create_auto_cdc_flow(
  target = "sales_enr",
  source = "sales_enr_view",    # streaming view as source since we've applied transformation in it
  keys = ["sales_id"],
  sequence_by = col("sale_timestamp"),
  apply_as_deletes = None,
  apply_as_truncates = None,
  except_column_list = None,
  stored_as_scd_type = 1         # SCD type 1 is also known as UPSERT
)