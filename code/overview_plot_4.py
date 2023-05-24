import os
import seaborn as sns
import scipy.stats as stats
import numpy as np
import pandas as pd
from configs import overview
import matplotlib.pyplot as plt

"""
Given a gender, plot bar plots accross age groups for different suicide methods.
"""

def bar_plot(path, gender, age_colms):
    df_main = pd.read_csv(path)

    N_age_groups = 9
    bars = np.arange(N_age_groups)
    bar_width = 0.1

    total_poi = []
    total_hang=[]
    total_weapon=[]
    total_others=[]

    for age in age_colms:
        df_gender = df_main.loc[df_main["gender"]==gender]
        #df_gender = df_gender.loc[df_gender["year"]>=2008]

        # total
        df_total = df_gender.loc[df_gender["method"]=="Totalsuicides"]
        sum_total = df_total[age].sum()

        # poison
        df_poison = df_gender.loc[df_gender["method"]=="poisoning"]
        sum_poi = df_poison[age].sum()
        #total_poi.append(sum_poi)
        total_poi.append((sum_poi*100)/sum_total)

        # hang
        df = df_gender.loc[df_gender["method"]=="Hang"]
        sum_ = df[age].sum()
        #total_hang.append(sum_)
        total_hang.append((sum_*100)/sum_total)

        # weapons
        df = df_gender.loc[df_gender["method"]=="weapons"]
        sum_ = df[age].sum()
        #total_weapon.append(sum_)
        total_weapon.append((sum_*100)/sum_total)

        # other
        df = df_gender.loc[df_gender["method"]=="Othermethods"]
        sum_ = df[age].sum()
        #total_others.append(sum_)
        total_others.append((sum_*100)/sum_total)

    colors = ['b', 'r', 'g', 'm']
    plt.bar(bars-bar_width*2, total_poi, bar_width, label = "Poison", color=colors[0])
    plt.bar(bars-bar_width, total_hang, bar_width, label = "Hang", color=colors[1])
    plt.bar(bars, total_weapon, bar_width, label = "Weapons", color=colors[2])
    plt.bar(bars+bar_width, total_others, bar_width, label = "Others", color=colors[3])
    plt.xticks(bars, age_colms)
    plt.xlabel("Age Groups")
    plt.ylabel('Perc. suicides')
    plt.title(f"Suicides from different methods for {gender} across different age groups")
    plt.legend(title='Methods')
    plt.show()


def pie_chart(path, gender, age):
    df_main = pd.read_csv(path)

    df_gender = df_main.loc[df_main["gender"]==gender]
    df_gender = df_gender.loc[df_gender["year"]>2016]

    # total
    df_total = df_gender.loc[df_gender["method"]=="Totalsuicides"]
    sum_total = df_total[age].sum()

    # poison
    df_poison = df_gender.loc[df_gender["method"]=="poisoning"]
    sum_poi = df_poison[age].sum()
    per_poi = (sum_poi*100)/sum_total

    # hang
    df = df_gender.loc[df_gender["method"]=="Hang"]
    sum_ = df[age].sum()
    per_hang = (sum_*100)/sum_total

    # weapons
    df = df_gender.loc[df_gender["method"]=="weapons"]
    sum_ = df[age].sum()
    per_weapon = (sum_*100)/sum_total

    # other
    df = df_gender.loc[df_gender["method"]=="Othermethods"]
    sum_ = df[age].sum()
    per_other = (sum_*100)/sum_total

    labels = ["poison", "hang", "weapon", "other"]
    size = [per_poi, per_hang, per_weapon, per_other]
    colors = sns.color_palette('colorblind', 4)

    if age!= "total":
        plt.title(f'Suicide methods of {gender} of age {age}')
    else:
        plt.title(f'Suicide methods of {gender}')

    plt.gca().set_aspect('equal')  # Set aspect ratio to make it a circle
    plt.pie(size, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
    plt.show()

if __name__ == '__main__':
    age_colms = ["0 - 19", "20 - 29", "30 - 39", "40 - 49", "50 - 59", "60 - 69", "70 - 79", "80 - 89", "90 +"]
    #bar_plot(overview.INPATH, "both", age_colms)

    # make pie chart for women
    # pie_chart(overview.INPATH, "Women", age_colms[0])
    # pie_chart(overview.INPATH, "Women", age_colms[1])
    # pie_chart(overview.INPATH, "Women", age_colms[2])
    # pie_chart(overview.INPATH, "Women", age_colms[3])
    # pie_chart(overview.INPATH, "Women", age_colms[4])
    # pie_chart(overview.INPATH, "Women", age_colms[5])
    # pie_chart(overview.INPATH, "Women", age_colms[6])
    # pie_chart(overview.INPATH, "Women", age_colms[7])
    # pie_chart(overview.INPATH, "Women", age_colms[8])


    # make pie chart for men
    # pie_chart(overview.INPATH, "Men", age_colms[0])
    # pie_chart(overview.INPATH, "Men", age_colms[1])
    # pie_chart(overview.INPATH, "Men", age_colms[2])
    # pie_chart(overview.INPATH, "Men", age_colms[3])
    # pie_chart(overview.INPATH, "Men", age_colms[4])
    # pie_chart(overview.INPATH, "Men", age_colms[5])
    # pie_chart(overview.INPATH, "Men", age_colms[6])
    # pie_chart(overview.INPATH, "Men", age_colms[7])
    # pie_chart(overview.INPATH, "Men", age_colms[8])

    # make pie chart for total 
    pie_chart(overview.INPATH, "Men", "total")
    pie_chart(overview.INPATH, "Women", "total")
