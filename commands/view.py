import pandas as pd
import os


def view(args):
    print(f"loading {args.i}...")
    df = pd.read_csv(args.i)

    # print("\nloaded csv file into pandas")

    # file size
    file_size = os.path.getsize(args.i)
    print(f"\nthe file size is: {file_size} bytes.\n")

    # top 2 rows
    # head = df.head(2)
    print(df.head(2))


    



