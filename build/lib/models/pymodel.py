
import pandas as pd 
import numpy as np
import snowflake.snowpark as snowpark
import logging
import sys
from snowflake.snowpark import Session
from jaffle_shop.utils import simple_scoring_system
# Define your scoring function


connection_parameters = {
    "account":"btpbxkt-th59875",
    "user": "mohammed",
    "password": "Bb65662/medart!",
    "role": "ACCOUNTADMIN",  
    "warehouse": "COMPUTE_WH",  
    "database": "JAFFLE_SHOP", 
    "schema": "dev",  
  }  

new_session = Session.builder.configs(connection_parameters).create()

new_session.add_import("utils.py", import_path="jaffle_shop.utils")


print(simple_scoring_system(30))