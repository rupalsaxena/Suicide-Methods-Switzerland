import os
import pandas as pd
from configs import preprocess as config

def preprocess_data(config):
    raw_path = config.RAWPATH
    files = os.listdir(raw_path)
    df = pd.DataFrame()
    for file_ in files:
        if file_.endswith("csv"):
            raw_file = os.path.join(raw_path, file_)
            raw_df = pd.read_csv(raw_file, header=6)
            raw_df = raw_df.drop(config.NaN_rows)
            col_names = raw_df.columns.tolist()
            col_names[0] = 'gender'
            col_names[10] = "total"
            raw_df.columns = col_names
            raw_df["year"] = file_.split(".")[0]
            raw_df["method"] = config.method_col
            raw_df = raw_df.drop([1, 5, 9, 13, 17, 21])
            raw_df = raw_df.reset_index(drop=True)
            raw_df["gender"] = raw_df["gender"].replace("Männer", "Men")
            raw_df["gender"] = raw_df["gender"].replace("Frauen", "Women")
            df = pd.concat([df, raw_df])
    df = df.reset_index(drop=True)
    df.to_csv(config.OUTPATH)
preprocess_data(config)
