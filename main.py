import pandas as pd
def modifySalaryColumn(df: pd.DataFrame) -> pd.DataFrame:
    df['salary'] = df['salary'] * 2
    return df

a = 0
b = 1