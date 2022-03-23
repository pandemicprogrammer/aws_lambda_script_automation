# Python script automator utilizing Pandas, AWS Lambda, environment variables
# Marie Valentonis 3/20/2022


import pandas as pd
import os

# import the ‘os’ package and replace the hard coded variables with os.environ[‘VARIABLE_NAME’]

def somefunction(df):
    new_df = df.T()
    
    
def run(event, context):
    df = pd.read_csv(os.environ['CSV_PATH'])
    transformed_df = somefunction(df)
    transformed_df.to_csv(os.environ['NEW_CSV_PATH'])
    
    