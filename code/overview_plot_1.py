import os
import pandas as pd
from configs import overview
import matplotlib.pyplot as plt


def overview_plot_1(path):
    """Defination: accross years, percent of deaths from suicides for different genders
    -> x axis: years, y axis: percent of deaths"""
    df = pd.read_csv(path)

    years = df["year"].unique().tolist()
    per_death_both = []
    per_death_women = []
    per_death_men = []
    
    for year in years:
        df_year = df.loc[df["year"]==year]
        suicide_both = df_year.loc[(df_year["method"]=="Totalsuicides") & (df_year["gender"]=="both"), "total"].values[0]
        all_both = df_year.loc[(df_year["method"]=="Allcausesofdeath") & (df_year["gender"]=="both"), "total"].values[0]
        per_both = (suicide_both * 100)/all_both
        per_death_both.append(per_both)

        suicide_women = df_year.loc[(df_year["method"]=="Totalsuicides") & (df_year["gender"]=="Women"), "total"].values[0]
        all_women = df_year.loc[(df_year["method"]=="Allcausesofdeath") & (df_year["gender"]=="Women"), "total"].values[0]
        per_women = (suicide_women * 100)/all_women
        per_death_women.append(per_women)

        suicide_men = df_year.loc[(df_year["method"]=="Totalsuicides") & (df_year["gender"]=="Men"), "total"].values[0]
        all_men = df_year.loc[(df_year["method"]=="Allcausesofdeath") & (df_year["gender"]=="Men"), "total"].values[0]
        per_men = (suicide_men * 100)/all_men
        per_death_men.append(per_men)
    
    df_sucide = pd.DataFrame()
    df_sucide["year"] = years
    df_sucide["together"] = per_death_both
    df_sucide["women"] = per_death_women
    df_sucide["men"] = per_death_men
    df_sucide = df_sucide.sort_values(by='year')

    # plot
    df_sucide.plot(x='year', y=["together", "women", "men"], color= ['yellow', 'blue', 'red'], kind='line', marker='o', figsize=(10, 6))
    plt.xlabel('Years')
    plt.ylabel('Percentage')
    plt.title('Percentage of Deaths from Suicide over years')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    overview_plot_1(overview.INPATH)

