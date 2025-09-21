import dlt
from pyspark.sql.functions import *
from pyspark.sql.types import *

# Creating Streaming View for Products Transformations

@dlt.view(
    name = 'products_enr_view'
)
def products_enr_view():
    df = spark.readStream.table('products_stg')
    df.withColumn('price', col('price').cast(IntegerType()))
    return df

# Creating Empty Streaming Table for Products
dlt.create_streaming_table(
    name = 'products_enr'
)   
# Creating auto cdc flow to UPSERT the records in silver table
dlt.create_auto_cdc_flow(
  target = "products_enr",
  source = "products_enr_view",    # streaming view as source since we've applied transformation in it
  keys = ["product_id"],
  sequence_by = col("last_updated"),
  apply_as_deletes = None,
  apply_as_truncates = None,
  except_column_list = None,
  stored_as_scd_type = 1         # SCD type 1 is also known as UPSERT
)