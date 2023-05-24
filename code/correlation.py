import os
import pandas as pd
from configs import overview
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

def find_correlation(path):
    df = pd.read_csv(path)

    # encode year
    df['year'] = df['year']-2000
    df = pd.get_dummies(df)
    df = df.rename(columns={'method_Allcausesofdeath': 'Allcausesofdeath'})
    df = df.rename(columns={'method_Hang': 'Hang'})
    df = df.rename(columns={'method_Othermethods': 'Othermethods'})
    df = df.rename(columns={'method_poisoning': 'poisoning'})
    df = df.rename(columns={'method_weapons': 'weapons'})
    df = df.rename(columns={'method_Totalsuicides': 'Totalsuicides'})
    df = df.rename(columns={'gender_Men': 'Men'})
    df = df.rename(columns={'gender_Women': 'Women'})
    df = df.rename(columns={'gender_both': 'People'})
    corr_matrix = df.corr()

    # Plot the correlation matrix
    sns.heatmap(corr_matrix, annot=True, cmap='viridis',fmt=".2f")
    plt.title('Correlation Matrix')
    plt.show()

if __name__ == '__main__':
    find_correlation(overview.INPATH)