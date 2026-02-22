import pandas as pd
import logging
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
orders_path = os.path.join(BASE_DIR, "orders.csv")

orders = pd.read_csv(orders_path)

logging.basicConfig(filename='error_log.txt', level=logging.INFO)

def clean_orders(orders_df):
    # Drop missing customer_id
    orders_df = orders_df.dropna(subset=['customer_id'])

    # Remove negative quantity
    orders_df = orders_df[orders_df['quantity'] > 0]

    # Remove duplicate order_id
    orders_df = orders_df.drop_duplicates(subset=['order_id'])

    # Fix date format
    orders_df['order_date'] = pd.to_datetime(
        orders_df['order_date'],
        errors='coerce'
    )

    # Remove invalid dates
    orders_df = orders_df.dropna(subset=['order_date'])

    return orders_df

def transform_data(orders_df, products_df):
    merged = pd.merge(
        orders_df,
        products_df,
        on='product_id',
        how='left'
    )

    merged['total_amount'] = merged['quantity'] * merged['price']

    return merged

def city_revenue(df):
    return df.groupby('city')['total_amount'].sum().reset_index()

if __name__ == "__main__":
    orders = pd.read_csv("orders.csv")
    products = pd.read_csv("products.csv")

    cleaned = clean_orders(orders)
    transformed = transform_data(cleaned, products)
    revenue = city_revenue(transformed)

    transformed.to_csv("cleaned_orders.csv", index=False)
    revenue.to_csv("city_revenue.csv", index=False)

    print("Pipeline executed successfully 🚀")