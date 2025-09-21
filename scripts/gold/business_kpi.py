import dlt
from pyspark.sql.functions import *

# CREATING A MAT BUSINESS VIEW

@dlt.table(
    name = 'business_sales_agg'
)
def business_sales_agg():

    df_factSales = spark.read.table('fact_sales')
    df_dimProd = spark.read.table('dim_products')
    df_dimCustd = spark.read.table('dim_customers')

    df_join = df_factSales.join(df_dimProd, df_factSales.product_id == df_dimProd.product_id) \
                    .join(df_dimCustd, df_factSales.customer_id == df_dimCustd.customer_id)

    df_prun = df_join.select("region","category","total_amount")

    df_agg = df_prun.groupBy("region","category").agg(sum("total_amount").alias("total_sales"))

    return df_agg


   
  