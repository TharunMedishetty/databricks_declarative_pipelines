import dlt

# Produts Expectations

products_rules = {
    'rule_1' : 'product_id IS NOT NULL',
    'rule_2' : 'price >= 0'
}

# Creating Streaming Table for Products

@dlt.table(
    name = 'products_stg'
)
@dlt.expect_all_or_drop(products_rules) # Adding Expectation: Drop the records if query not satisfied with the defined rules
def products_stg():
    df = spark.readStream.table('dlt_tharun.source.products')
    return df

