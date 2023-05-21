from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import numpy as np

def decision_tree(X_train, X_test, y_train, y_test, scatter=False):
    regressor = DecisionTreeRegressor()
    regressor.fit(X_train, y_train)

    # predict train set
    y_train_pred = regressor.predict(X_train).tolist()
    if scatter:
        scatter_plot(y_train_pred, y_train.tolist(), testset=False)

    # predict test set
    y_pred = regressor.predict(X_test).tolist()
    r2 = r2_score(y_test.tolist(), y_pred)
    print("r square: ", r2)
    if scatter:
        scatter_plot(y_pred, y_test.tolist())

    return regressor

def scatter_plot(y_pred, y_test, testset=True):
    plt.scatter(y_pred, y_test, marker="x", label="suicides/deaths")

    x = np.linspace(0, 80000, num=2)
    y = x
    plt.plot(x, y, color='r', label='y=x')
    plt.legend()

    plt.xlabel('predictions')
    plt.ylabel('true values')

    if testset:
        plt.title('True values and predictions on decision tree model on test set')
    else:
        plt.title('True values and predictions on decision tree model on train set')

    plt.show()


    