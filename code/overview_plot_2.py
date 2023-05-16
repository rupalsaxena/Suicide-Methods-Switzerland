import os
import pandas as pd
from configs import overview
import matplotlib.pyplot as plt

def overview_plot_2(path, gender):
    """
    Percentage of suicides from different methods accross years
    """
    df = pd.read_csv(path)
    years = df["year"].unique().tolist()
    poison = []
    hang = []
    weapons = []
    other = []
    for year in years:
        df_year = df.loc[df["year"]==year]
        print(df_year.head(40))

        # poisoning
        yr_poison = df_year.loc[(df_year["method"]=="poisoning") & (df_year["gender"]==gender), "total"].values[0]
        yr_suicide = df_year.loc[(df_year["method"]=="Totalsuicides") & (df_year["gender"]==gender), "total"].values[0]
        per_poi = (yr_poison*100)/yr_suicide
        poison.append(per_poi)

        # hang
        yr_hang = df_year.loc[(df_year["method"]=="Hang") & (df_year["gender"]==gender), "total"].values[0]
        per_hang = (yr_hang*100)/yr_suicide
        hang.append(per_hang)

        # weapons
        yr_weapon = df_year.loc[(df_year["method"]=="weapons") & (df_year["gender"]==gender), "total"].values[0]
        per_weapon = (yr_weapon*100)/yr_suicide
        weapons.append(per_weapon)

        # other
        yr_other = df_year.loc[(df_year["method"]=="Othermethods") & (df_year["gender"]==gender), "total"].values[0]
        per_other = (yr_other*100)/yr_suicide
        other.append(per_other)
 
    fin_df = pd.DataFrame()
    fin_df["year"] = years
    fin_df["Poisoning"] = poison
    fin_df["Hang"] = hang
    fin_df["Weapons"] = weapons
    fin_df["Other"] = other
    fin_df = fin_df.sort_values(by='year')

    # plot
    fin_df.plot(x='year', y=["Poisoning", "Hang", "Weapons", "Other"], color= ['pink', 'blue', 'red', "yellow"], kind='line', figsize=(10, 6))
    plt.xlabel('Years')
    plt.ylabel('Percentage')
    plt.title('Percentage of suicides from different methods accross years for Women')
    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    overview_plot_2(overview.INPATH, "Women")