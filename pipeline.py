#pipeline.py
import pandas as pd

# We will do some cleanup on column names, drop columns that are not needed and impute age to repace missing values with the mean
def process_data(df: pd.DataFrame) -> pd.DataFrame:
    
    df_output = df.rename({i:i.replace("'","").lower() for i in df.columns.to_list()}, axis = 1) \
    .drop(columns = ['name', 'ticket','home.dest','boat','body'])

    df_output = df_output.rename(columns = {"id": "passengerid"})

    df_output['age'] = pd.to_numeric(df_output['age'], errors='coerce')

    # Correct line of code
    #df_output = df_output.assign(age = lambda x: x.age.fillna(x.age.mean()).astype('int'))

    # Code with bug
    df = df_output.assign(age = lambda x: x.age.fillna(x.age.mean()).astype('int'))
        
    return df_output
def run_pipeline(input_path: str, output_path: str, save = True) -> pd.DataFrame:
    
    df = pd.read_csv(input_path)
    df_processed = process_data(df)
    
    if save:
        df_processed.to_csv(output_path, index = False)
    
    return df_processed