import dlt

# Sales Expectations

sales_rules = {
    'rule_1' : 'sales_id IS NOT NULL'
}

# Empty Streaming Table

dlt.create_streaming_table(
    name = 'sales_stg',
    expect_all_or_drop = sales_rules # Adding Expectation: Drop the records if query not satisfied with the defined rules
)

# Creating East Sales Flow
# Now returned df from the east_sales function is appends to the streaming table that we've specified in the target for append flow.
@dlt.append_flow(target='sales_stg')
def east_sales():

    df = spark.readStream.table('dlt_tharun.source.sales_east')
    return df

# Creating West Sales Flow
@dlt.append_flow(target='sales_stg')
def west_sales():

    df = spark.readStream.table('dlt_tharun.source.sales_west')
    return df

