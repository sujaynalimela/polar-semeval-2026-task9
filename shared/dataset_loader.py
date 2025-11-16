import pandas as pd
from datasets import Dataset

def load_dataset(path):
    df = pd.read_csv(path)
    return Dataset.from_pandas(df)

