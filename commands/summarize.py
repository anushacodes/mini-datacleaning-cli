import pandas as pd
from skimpy import skim

def summarize(args):
    df = pd.read_csv(args.i)
    print(skim(df))