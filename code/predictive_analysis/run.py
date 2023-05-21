import os
import numpy as np
import pandas as pd
import config
from prepare_data import prepare_train_data as prep_train
from prepare_data import prepare_future_data as prep_future
from models import decision_tree
"""
TODO: plot future predictions
TODO: plot correlation matrix for features
"""


def run():
    # train model
    X_train, X_test, Y_train, Y_test = prep_train(config)
    model = decision_tree(X_train, X_test, Y_train, Y_test, scatter=True)

    # predict future
    X_pure, X_enc = prep_future(config)
    y_pred = model.predict(X_enc)

    # write results in df
    df_future = X_pure
    df_future["suicides"] = y_pred.tolist()
    df_future.to_csv(config.OUTPATH, index=False)
    print(df_future)

if __name__ == '__main__':
    run()