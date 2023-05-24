from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge, Lasso
from sklearn.metrics import r2_score
from sklearn.svm import SVR
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xgboost as xgb
import config

def decision_tree(X_train, X_test, y_train, y_test, scatter=False):
    regressor = DecisionTreeRegressor()
    regressor.fit(X_train, y_train)

    # predict train set
    y_train_pred = regressor.predict(X_train).tolist()
    r2 = r2_score(y_train.tolist(), y_train_pred)
    print("r square decision tree trainset: ", r2)
    if scatter:
        scatter_plot(y_train_pred, y_train.tolist(), testset=False)

    # predict test set
    y_pred = regressor.predict(X_test).tolist()
    r2 = r2_score(y_test.tolist(), y_pred)
    print("r square decision tree testset: ", r2)
    if scatter:
        scatter_plot(y_pred, y_test.tolist())

    return regressor

def model(X_train, X_test, y_train, y_test, scatter=False, model="RF", fit_full = False):
    if model=="RF": # random forest
        regressor = RandomForestRegressor(n_estimators=10, random_state=42)
    elif model=="DT": # decision tree
        regressor = DecisionTreeRegressor()
    elif model=="LR": # linear regression
        regressor = LinearRegression()
    elif model=="xgb": # xgboost
        regressor = xgb.XGBRegressor()
    elif model=="svr": # support vector regression
        regressor = SVR(kernel='rbf', C=1.0, epsilon=0.1)
    elif model=="rr": # ridge regresion
        regressor = Ridge(alpha=0.1)
    elif model=="lasso_r": # lasso regression
        regressor = Lasso(alpha=0.01)

    regressor.fit(X_train, y_train)

    # predict train set
    y_train_pred = regressor.predict(X_train).tolist()
    r2 = r2_score(y_train.tolist(), y_train_pred)
    mse = mean_squared_error(y_train.tolist(), y_train_pred)
    print(f"r square {model} trainset: ", r2)
    print(f"mse {model}  trainset: ", mse)

    # del later
    df_train_ = pd.DataFrame(data = {"y_pred": y_train_pred, "y_train": y_train.tolist()})
    print(df_train_.head(40))

    if scatter:
        scatter_plot(y_train_pred, y_train.tolist(), testset=False, method=model)

    # predict test set
    y_pred = regressor.predict(X_test).tolist()


    # del later
    df_test_ = pd.DataFrame(data = {"y_pred": y_pred, "y_test": y_test.tolist()})
    print(df_test_.head(40))


    r2 = r2_score(y_test.tolist(), y_pred)
    mse = mean_squared_error(y_test.tolist(), y_pred)
    print(f"r square {model} testset: ", r2)
    print(f"mse {model} testset: ", mse)

    if scatter:
        scatter_plot(y_pred, y_test.tolist(), method=model)
    
    # fit on full data
    X_full = pd.concat([X_train, X_test], ignore_index=True)
    y_full = pd.concat([y_train, y_test], ignore_index=True)

    if fit_full:
        if model=="RF": # random forest
            regressor = RandomForestRegressor(n_estimators=10, random_state=42)
        elif model=="DT": # decision tree
            regressor = DecisionTreeRegressor()
        elif model=="LR": # linear regression
            regressor = LinearRegression()
        elif model=="xgb": # xgboost
            regressor = xgb.XGBRegressor()
        elif model=="svr": # support vector regression
            regressor = SVR(kernel='rbf', C=1.0, epsilon=0.1)
        elif model=="rr": # ridge regresion
            regressor = Ridge(alpha=0.1)
        elif model=="lasso_r": # lasso regression
            regressor = Lasso(alpha=0.1)

        regressor.fit(X_full, y_full)

    return regressor


def scatter_plot(y_pred, y_test, testset=True, method="DT"):
    age_grp = config.choose_col[3]
    if age_grp == "total":
        age_grp = "all"
        x = np.linspace(0, 600, num=2)
    else:
        x = np.linspace(0, 100, num=2)

    plt.scatter(y_pred, y_test, marker="x", label="suicides/deaths")

    
    y = x
    plt.plot(x, y, color='r', label='y=x')
    plt.legend()

    plt.xlabel('predictions')
    plt.ylabel('true values')

    if testset:
        plt.title(f'True values and predictions on {method} model on test set for {age_grp} age group')
    else:
        plt.title(f'True values and predictions on {method} model on train set for {age_grp} age group')

    plt.show()


    