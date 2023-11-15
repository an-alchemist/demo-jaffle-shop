
import sys
sys.path.insert(0, '..')
import pandas as pd 
import numpy as np
import snowflake.snowpark as snowpark
import logging
import sys
from snowflake.snowpark import Session

# Define your scoring function

def model(dbt, session):
    dbt.config(
        materialized = "table",
        packages = ["pandas", "numpy"],
        imports = ["@demo/utils.py"]
    )
    from utils import simple_scoring_system


    df = pd.DataFrame({
        'random_numbers': np.random.rand(10)  # Generates 10 random numbers
        
    })

    # Apply the scoring function to the DataFrame
    df['score'] = df['random_numbers'].apply(simple_scoring_system)

    return df
