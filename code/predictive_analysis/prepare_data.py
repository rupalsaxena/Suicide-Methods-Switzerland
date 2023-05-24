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


    # exp 1 and exp 2
    # df_main = df_main[df_main['method'] != 'Allcausesofdeath']
    # df_main = df_main[df_main['method'] != 'Totalsuicides']

    # exp 3
    df_main = df_main[df_main['method'] != 'Allcausesofdeath']
    df_main = df_main[df_main['method'] != 'weapons']
    df_main = df_main[df_main['method'] != 'Hang']
    df_main = df_main[df_main['method'] != 'Othermethods']
    df_main = df_main[df_main['method'] != 'poisoning']

    df_main = df_main.reset_index(drop=True)

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



    # split the data for some years as test and train
    df_train = df_main.loc[df_main["enc_year"]<=17]
    df_test = df_main.loc[df_main["enc_year"]>17]

    X_train = df_train.drop([config.choose_col[3]], axis=1)
    X_test =  df_test.drop([config.choose_col[3]], axis=1)
    Y_train = df_train[config.choose_col[3]]
    Y_test = df_test[config.choose_col[3]]

    return X_train, X_test, Y_train, Y_test

def prepare_future_data(config):
    df_pure = pd.DataFrame(config.data, columns=config.cols)

    # # exp 1 and exp 2
    # df_pure = df_pure[df_pure['method'] != 'Allcausesofdeath']
    # df_pure = df_pure[df_pure['method'] != 'Totalsuicides']


    # exp 3
    df_pure = df_pure[df_pure['method'] != 'Allcausesofdeath']
    df_pure = df_pure[df_pure['method'] != 'weapons']
    df_pure = df_pure[df_pure['method'] != 'Hang']
    df_pure = df_pure[df_pure['method'] != 'Othermethods']
    df_pure = df_pure[df_pure['method'] != 'poisoning']



    df_pure = df_pure.reset_index(drop=True)


    # one hot encode method
    encoder = OneHotEncoder(sparse=False)
    encoded_data = encoder.fit_transform(df_pure[['method']])
    encoded_df = pd.DataFrame(encoded_data, columns=encoder.categories_[0])
    df_enc = pd.concat([df_pure, encoded_df], axis=1)

    # one hot encode gender
    encoded_data = encoder.fit_transform(df_enc[['gender']])
    encoded_df = pd.DataFrame(encoded_data, columns=encoder.categories_[0])
    df_enc = pd.concat([df_enc, encoded_df], axis=1)

    df_enc['year'] = df_enc['year'].replace(2022, 22.00)
    df_enc['year'] = df_enc['year'].replace(2023, 23.00)
    df_enc['year'] = df_enc['year'].replace(2024, 24.00)
    df_enc['year'] = df_enc['year'].replace(2025, 25.00)
    df_enc['year'] = df_enc['year'].replace(2026, 26.00)
    enc_year = df_enc['year'].tolist()


    df_enc = df_enc.drop(['method', 'gender', 'year'], axis=1)
    df_enc["enc_year"] = enc_year
    df_enc["enc_year"] = df_enc["enc_year"].astype(float)

    return df_pure, df_enc


if __name__ == '__main__':
    # X_train, X_test, Y_train, Y_test = prepare_train_data(config)
    future_data = prepare_future_data(config)
