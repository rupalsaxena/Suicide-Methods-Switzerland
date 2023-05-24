import os
import numpy as np
import pandas as pd
import config
from prepare_data import prepare_train_data as prep_train
from prepare_data import prepare_future_data as prep_future
from models import model


def run():
    # get data
    X_train, X_test, Y_train, Y_test = prep_train(config)

    # train model
    #model_ = model(X_train, X_test, Y_train, Y_test, scatter=True, model="RF", fit_full=True)
    model_ = model(X_train, X_test, Y_train, Y_test, scatter=True, model="xgb", fit_full=True)

    # predict future
    X_pure, X_enc = prep_future(config)
    y_pred = model_.predict(X_enc)

    # enforcing minimum death = 0
    minimum_value = 0.0
    y_pred = np.maximum(y_pred, minimum_value)

    # write results in df
    df_future = X_pure
    df_future["suicides"] = y_pred.tolist()
    df_future.to_csv(config.OUTPATH, index=False)
    print(df_future)

if __name__ == '__main__':
    run()