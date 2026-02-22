import pandas as pd
from pipeline import clean_orders

def test_negative_quantity_removed():
    df = pd.DataFrame({
        "order_id": [1],
        "customer_id": [101],
        "product_id": [1001],
        "quantity": [-2],
        "order_date": ["2024-01-10"],
        "city": ["Delhi"]
    })

    cleaned = clean_orders(df)

    assert cleaned.empty