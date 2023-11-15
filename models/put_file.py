
import sys
sys.path.insert(0, '..')
import pandas as pd 
import numpy as np
import snowflake.snowpark as snowpark
import logging
import sys
from snowflake.snowpark import Session

# Define your scoring function


connection_parameters = {
    "account":"XXXXXX",
    "user": "XXXXX",
    "password": "CXXXXXX!",
    "role": "ACCOUNTADMIN",  
    "warehouse": "COMPUTE_WH",  
    "database": "JAFFLE_SHOP", 
    "schema": "dev",  
  }  

new_session = Session.builder.configs(connection_parameters).create()

new_session.file.put('utils.py', "@demo/", auto_compress=False  )

