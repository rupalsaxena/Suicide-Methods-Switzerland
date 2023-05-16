import os
import pandas as pd
from configs import preprocess as config

def preprocess_data(config):
    raw_path = config.RAWPATH
    files = os.listdir(raw_path)
    df = pd.DataFrame()
    for file_ in files:
        if file_.endswith("csv"):
            # read file
            raw_file = os.path.join(raw_path, file_)
            raw_df = pd.read_csv(raw_file, header=6)
            raw_df = raw_df.drop(config.NaN_rows)

            # updating col names
            col_names = raw_df.columns.tolist()
            col_names[0] = 'gender'
            col_names[10] = "total"
            raw_df.columns = col_names

            # adding year
            raw_df["year"] = file_.split(".")[0]

            # adding method column
            raw_df["method"] = config.method_col

            # replace gender column names
            raw_df["gender"] = raw_df["gender"].replace("Alle Todesursachen", "both")
            raw_df["gender"] = raw_df["gender"].replace("Übrige Suizidmethoden", "both")
            raw_df["gender"] = raw_df["gender"].replace("Schusswaffen", "both")
            raw_df["gender"] = raw_df["gender"].replace("Erhängen", "both")
            raw_df["gender"] = raw_df["gender"].replace("Vergiftung 1)", "both")
            raw_df["gender"] = raw_df["gender"].replace("Vergiftung", "both")
            raw_df["gender"] = raw_df["gender"].replace("Anzahl Suizide insgesamt", "both")
            raw_df["gender"] = raw_df["gender"].replace("Männer", "Men")
            raw_df["gender"] = raw_df["gender"].replace("Frauen", "Women")

            df = pd.concat([df, raw_df])

    # clean the data
    # replacing - values to 0
    df = df.replace("- ", 0)
    # make data consistent by removing "," and " " from values and converting them to float
    columns = df.columns
    for column in columns:
        df[column] = df[column].astype(str)
        df[column]= df[column].str.replace(' ', '', regex=True)
        df[column]= df[column].str.replace(',', '', regex=True)
        if column != "method" and column != "gender" and column != "year":
            df[column] = df[column].astype(float)
    
    df["year"] = df["year"].astype(int)

    # write the file
    df = df.reset_index(drop=True)
    df.to_csv(config.OUTPATH, index=False)

preprocess_data(config)
