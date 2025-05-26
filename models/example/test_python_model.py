# models/example_python_model.py

def model(dbt, session):
    dbt.config(
        materialized="table"
    )

    # Create a simple pandas DataFrame
    import pandas as pd

    df = pd.DataFrame({
        'id': [1, 2, 3],
        'value': ['one', 'two', 'three']
    })

    return df
