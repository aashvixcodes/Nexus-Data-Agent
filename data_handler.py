import pandas as pd
from faker import Faker

def load_mock_data():
    """Load mock sales data from CSV."""
    return pd.read_csv('mock_sales_data.csv')

def generate_mock_data(rows=10):
    """Generate additional mock data using Faker."""
    fake = Faker()
    data = []
    for _ in range(rows):
        data.append({
            'Date': fake.date_this_year(),
            'Region': fake.random_element(['West', 'East']),
            'Discounts': fake.random_int(10, 25),
            'Revenue': fake.random_int(800000, 1000000),
            'SentimentScore': fake.random_element([-0.2, 0.1, 0.3])
        })
    return pd.DataFrame(data)