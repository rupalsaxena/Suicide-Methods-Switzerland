import os
import numpy as np
import pandas as pd
import config
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split

def prepare_train_data(config):
    # load data
    inpath = config.INPATH
    df_main = pd.read_csv(inpath)
    df_main = df_main[config.choose_col]

    # one hot encode method
    encoder = OneHotEncoder(sparse=False)
    encoded_data = encoder.fit_transform(df_main[['method']])
    encoded_df = pd.DataFrame(encoded_data, columns=encoder.categories_[0])
    df_main = pd.concat([df_main, encoded_df], axis=1)

    # one hot encode gender
    encoded_data = encoder.fit_transform(df_main[['gender']])
    encoded_df = pd.DataFrame(encoded_data, columns=encoder.categories_[0])
    df_main = pd.concat([df_main, encoded_df], axis=1)

    # ordinal encoding
    encoder = OrdinalEncoder()
    encoded_years = encoder.fit_transform(df_main[['year']])
    df_main['enc_year'] = encoded_years

    # drop not needed columns
    df_main = df_main.drop(['method', 'gender', 'year'], axis=1)

    df_dep = df_main[config.choose_col[3]]
    df_ind = df_main.drop([config.choose_col[3]], axis=1)

    # split the data into train and test
    X_train, X_test, Y_train, Y_test = train_test_split(df_ind, df_dep, test_size=0.1, random_state=42)

    return X_train, X_test, Y_train, Y_test

def prepare_future_data(config):
    df_pure = pd.DataFrame(config.data, columns=config.cols)

    # one hot encode method
    encoder = OneHotEncoder(sparse=False)
    encoded_data = encoder.fit_transform(df_pure[['method']])
    encoded_df = pd.DataFrame(encoded_data, columns=encoder.categories_[0])
    df_enc = pd.concat([df_pure, encoded_df], axis=1)

    # one hot encode gender
    encoded_data = encoder.fit_transform(df_enc[['gender']])
    encoded_df = pd.DataFrame(encoded_data, columns=encoder.categories_[0])
    df_enc = pd.concat([df_enc, encoded_df], axis=1)

    df_enc['enc_year'] = df_enc['year'].replace(2022, 22.00)
    df_enc['enc_year'] = df_enc['year'].replace(2023, 23.00)
    df_enc['enc_year'] = df_enc['year'].replace(2024, 24.00)
    df_enc['enc_year'] = df_enc['year'].replace(2025, 25.00)
    df_enc['enc_year'] = df_enc['year'].replace(2026, 26.00)

    df_enc = df_enc.drop(['method', 'gender', 'year'], axis=1)
    return df_pure, df_enc


if __name__ == '__main__':
    # X_train, X_test, Y_train, Y_test = prepare_train_data(config)
    future_data = prepare_future_data(config)
