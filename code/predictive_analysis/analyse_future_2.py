import os
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns


def overview_2(path, gender):
    df = pd.read_csv(path)
    years = df["year"].unique().tolist()

    perc_poi = []
    per_hang = []
    per_weapon = []
    per_other = []

    for year in years:
        df_year = df.loc[df["year"]==year]

        # select gender 
        df_gender = df_year.loc[df_year["gender"]==gender]


        # poi
        N = df_gender.loc[df_gender["method"]=="poisoning", "suicides"].values[0]
        total = df_gender["suicides"].sum()
        perc_poi.append(N*100/total)

        # hang
        N = df_gender.loc[df_gender["method"]=="Hang", "suicides"].values[0]
        total = df_gender["suicides"].sum()
        per_hang.append(N*100/total)

        # weapons
        N = df_gender.loc[df_gender["method"]=="weapons", "suicides"].values[0]
        total = df_gender["suicides"].sum()
        per_weapon.append(N*100/total)

        # others
        N = df_gender.loc[df_gender["method"]=="Othermethods", "suicides"].values[0]
        total = df_gender["suicides"].sum()
        per_other.append(N*100/total)

    df_sucide = pd.DataFrame()
    df_sucide["year"] = years
    df_sucide["Poison"] = perc_poi
    df_sucide["Hang"] = per_hang
    df_sucide["Weapon"] = per_weapon
    df_sucide["Others"] = per_other
    df_sucide = df_sucide.sort_values(by='year')

    # plot
    df_sucide.plot(
        x='year', y=["Poison", "Hang", "Weapon", "Others"], color= ['blue', 'red', 'pink', 'yellow'], kind='line', marker='o', figsize=(10, 6)
    )
    plt.xlabel('Years')
    plt.ylabel('Percentage')
    plt.title(f'Future predictions of percentage of suicides from different methods for {gender}')
    plt.grid(True)
    plt.legend()
    plt.show()


def pie_chart(path, year, age, gender):
    df = pd.read_csv(path)
    df_year = df.loc[df["year"]==year]
    df_gender = df_year.loc[df_year["gender"]==gender]

    # poi
    N = df_gender.loc[df_gender["method"]=="poisoning", "suicides"].values[0]
    total = df_gender["suicides"].sum()
    size_poi = N*100/total

    # hang
    N = df_gender.loc[df_gender["method"]=="Hang", "suicides"].values[0]
    total = df_gender["suicides"].sum()
    size_hang = N*100/total

    # weapons
    N = df_gender.loc[df_gender["method"]=="weapons", "suicides"].values[0]
    total = df_gender["suicides"].sum()
    size_weap = N*100/total

    # others
    N = df_gender.loc[df_gender["method"]=="Othermethods", "suicides"].values[0]
    total = df_gender["suicides"].sum()
    size_other = N*100/total

    # plot
    labels = ["poison", "hang", "weapon", "other"]
    size = [size_poi, size_hang, size_weap, size_other]
    colors = sns.color_palette('colorblind', 4)

    if age != "total":
        plt.title(f'Predicted Suicide methods of {gender} of age {age} in {str(year)}')
    else:
        plt.title(f'Predicted Suicide methods of {gender} in {str(year)}')

    plt.gca().set_aspect('equal')  # Set aspect ratio to make it a circle
    plt.pie(size, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
    plt.show()


if __name__ == '__main__':
    # exp 1
    # PATH = "/Users/rupal/Documents/GitHub/Suicide-Methods-Switzerland/dataset/future_all_ages.csv"
    # pie_chart(PATH, 2024, "all", "Women")
    # pie_chart(PATH, 2024, "all", "Men")

    #overview_2(PATH, "Women")

    # exp: 2
    PATH = "/Users/rupal/Documents/GitHub/Suicide-Methods-Switzerland/dataset/future_20_29_ages.csv"
    pie_chart(PATH, 2024, "20-29", "Women")
    pie_chart(PATH, 2024, "20-29", "Men")