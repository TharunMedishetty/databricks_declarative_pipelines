import dlt
from pyspark.sql.functions import *

# Create an empty streaming table

dlt.create_streaming_table(
    name = 'fact_sales'
)

# We are using sales_enr_view as source instead of sales_enr table since this table can be updated bz of UPSERT. 
# And, for streaming table source should be append only, not the update.
# sales_enr_view is a streaming view and it brings only new data.

# AUTO CDC FLOW

dlt.create_auto_cdc_flow(
  target = "fact_sales",
  source = "sales_enr_view",    # streaming view as source since we've applied transformation in it
  keys = ["sales_id"],
  sequence_by = col("sale_timestamp"),
  apply_as_deletes = None,
  apply_as_truncates = None,
  except_column_list = None,
  stored_as_scd_type = 1       # SCD type 1
)