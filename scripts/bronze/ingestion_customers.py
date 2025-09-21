import dlt

# Customer Expectations
customers_rules = {
    'rule_1' : 'customer_id IS NOT NULL',
    'rule_2' : 'customer_name IS NOT NULL'
}

# Creating Streaming Table for Customers

@dlt.table(
    name = 'customers_stg'
)
@dlt.expect_all_or_drop(customers_rules) # Adding Expectation: Drop the records if query not satisfied with the defined rules
def customers_stg():

    df = spark.readStream.table('dlt_tharun.source.customers')
    return df