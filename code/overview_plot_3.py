import os
import seaborn as sns
import scipy.stats as stats
import numpy as np
import pandas as pd
from configs import overview
import matplotlib.pyplot as plt

def bar_plot(path, years, gender):
    """
    bar plot for different years with each bar in one year represents suicide percentage by age. 
    """
    df = pd.read_csv(path)
    bars = np.arange(len(years))
    width = 0.1

    age_0_19 = []
    age_20_29 = []
    age_30_39 = []
    age_40_49 = []
    age_50_59 = []
    age_60_69 = []
    age_70_79 = []   
    age_80_89 = []  
    age_90_plus = []

    for year in years:
        df_year = df.loc[df["year"]==year]
        
        # 0-19
        N_0_19 = df_year.loc[(df_year["gender"]==gender) & (df_year["method"]=="Totalsuicides"), "0 - 19"].values[0]
        deaths = df_year.loc[(df_year["gender"]==gender) & (df_year["method"]=="Allcausesofdeath"), "0 - 19"].values[0]
        per_0_19 = (N_0_19*100)/deaths
        age_0_19.append(per_0_19)

        # 20-29
        N_20_29 = df_year.loc[(df_year["gender"]==gender) & (df_year["method"]=="Totalsuicides"), "20 - 29"].values[0]
        deaths = df_year.loc[(df_year["gender"]==gender) & (df_year["method"]=="Allcausesofdeath"), "20 - 29"].values[0]
        per_20_29 = (N_20_29*100)/deaths
        age_20_29.append(per_20_29)

        # 30-39
        N_30_39 = df_year.loc[(df_year["gender"]==gender) & (df_year["method"]=="Totalsuicides"), "30 - 39"].values[0]
        deaths = df_year.loc[(df_year["gender"]==gender) & (df_year["method"]=="Allcausesofdeath"), "30 - 39"].values[0]
        per_30_39 = (N_30_39*100)/deaths
        age_30_39.append(per_30_39)

        # 40-49
        N_40_49 = df_year.loc[(df_year["gender"]==gender) & (df_year["method"]=="Totalsuicides"), "40 - 49"].values[0]
        deaths = df_year.loc[(df_year["gender"]==gender) & (df_year["method"]=="Allcausesofdeath"), "40 - 49"].values[0]
        per_40_49 = (N_40_49*100)/deaths
        age_40_49.append(per_40_49)

        # 50-59
        N_50_59 = df_year.loc[(df_year["gender"]==gender) & (df_year["method"]=="Totalsuicides"), "50 - 59"].values[0]
        deaths = df_year.loc[(df_year["gender"]==gender) & (df_year["method"]=="Allcausesofdeath"), "50 - 59"].values[0]
        per_50_59 = (N_50_59*100)/deaths
        age_50_59.append(per_50_59)

        # 60-69
        N = df_year.loc[(df_year["gender"]==gender) & (df_year["method"]=="Totalsuicides"), "60 - 69"].values[0]
        deaths = df_year.loc[(df_year["gender"]==gender) & (df_year["method"]=="Allcausesofdeath"), "60 - 69"].values[0]
        percent = (N*100)/deaths
        age_60_69.append(percent)

        # 70-79
        N = df_year.loc[(df_year["gender"]==gender) & (df_year["method"]=="Totalsuicides"), "70 - 79"].values[0]
        deaths = df_year.loc[(df_year["gender"]==gender) & (df_year["method"]=="Allcausesofdeath"), "70 - 79"].values[0]
        percent = (N*100)/deaths
        age_70_79.append(percent)

        # 80-89
        N = df_year.loc[(df_year["gender"]==gender) & (df_year["method"]=="Totalsuicides"), "80 - 89"].values[0]
        deaths = df_year.loc[(df_year["gender"]==gender) & (df_year["method"]=="Allcausesofdeath"), "80 - 89"].values[0]
        percent = (N*100)/deaths
        age_80_89.append(percent)

        # 90+
        N = df_year.loc[(df_year["gender"]==gender) & (df_year["method"]=="Totalsuicides"), "90 +"].values[0]
        deaths = df_year.loc[(df_year["gender"]==gender) & (df_year["method"]=="Allcausesofdeath"), "90 +"].values[0]
        percent = (N*100)/deaths
        age_90_plus.append(percent)

    # print(age_40_49)
    # print(age_50_59)
    # print(age_60_69)
    # print(age_70_79)
    # print(age_80_89)
    # print(age_90_plus)

    colors = ['b', 'r', 'g', 'm', 'y', 'c', 'k', 'pink', 'gray']
    plt.bar(bars-width*4, age_0_19, width, label = "0-19", color=colors[0])
    plt.bar(bars-width*3, age_20_29, width, label = "20-29", color=colors[1])
    plt.bar(bars-width*2, age_30_39, width, label = "30-39", color=colors[2])
    plt.bar(bars-width, age_40_49, width, label = "40-49", color=colors[3])
    plt.bar(bars, age_50_59, width, label = "50-59", color=colors[4])
    plt.bar(bars+width, age_60_69, width, label = "60-69", color=colors[5])
    plt.bar(bars+width*2, age_70_79, width, label = "70-79", color=colors[6])
    plt.bar(bars+width*3, age_80_89, width, label = "80-89", color=colors[7])
    plt.bar(bars+width*4, age_90_plus, width, label = "90+", color=colors[8])

    plt.xticks(bars+width, years)

    plt.xlabel("Years")
    plt.ylabel('perc. deaths from suicide')
    plt.title(f"Percentage of deaths from suicide for different age groups for {gender}")
    plt.legend(title='Ages')
    plt.show()


def boxplots(path, years, gender):
    """
    violin plots of percentage of deaths from suicide for different age groups
    """
    df = pd.read_csv(path)
    age_0_19 = []
    age_20_29 = []
    age_30_39 = []
    age_40_49 = []
    age_50_59 = []
    age_60_69 = []
    age_70_79 = []   
    age_80_89 = []  
    age_90_plus = []

    for year in years:
        df_year = df.loc[df["year"]==year]
        
        # 0-19
        N_0_19 = df_year.loc[(df_year["gender"]==gender) & (df_year["method"]=="Totalsuicides"), "0 - 19"].values[0]
        deaths = df_year.loc[(df_year["gender"]==gender) & (df_year["method"]=="Allcausesofdeath"), "0 - 19"].values[0]
        per_0_19 = (N_0_19*100)/deaths
        age_0_19.append(per_0_19)

        # 20-29
        N_20_29 = df_year.loc[(df_year["gender"]==gender) & (df_year["method"]=="Totalsuicides"), "20 - 29"].values[0]
        deaths = df_year.loc[(df_year["gender"]==gender) & (df_year["method"]=="Allcausesofdeath"), "20 - 29"].values[0]
        per_20_29 = (N_20_29*100)/deaths
        age_20_29.append(per_20_29)

        # 30-39
        N_30_39 = df_year.loc[(df_year["gender"]==gender) & (df_year["method"]=="Totalsuicides"), "30 - 39"].values[0]
        deaths = df_year.loc[(df_year["gender"]==gender) & (df_year["method"]=="Allcausesofdeath"), "30 - 39"].values[0]
        per_30_39 = (N_30_39*100)/deaths
        age_30_39.append(per_30_39)

        # 40-49
        N_40_49 = df_year.loc[(df_year["gender"]==gender) & (df_year["method"]=="Totalsuicides"), "40 - 49"].values[0]
        deaths = df_year.loc[(df_year["gender"]==gender) & (df_year["method"]=="Allcausesofdeath"), "40 - 49"].values[0]
        per_40_49 = (N_40_49*100)/deaths
        age_40_49.append(per_40_49)

        # 50-59
        N_50_59 = df_year.loc[(df_year["gender"]==gender) & (df_year["method"]=="Totalsuicides"), "50 - 59"].values[0]
        deaths = df_year.loc[(df_year["gender"]==gender) & (df_year["method"]=="Allcausesofdeath"), "50 - 59"].values[0]
        per_50_59 = (N_50_59*100)/deaths
        age_50_59.append(per_50_59)

        # 60-69
        N = df_year.loc[(df_year["gender"]==gender) & (df_year["method"]=="Totalsuicides"), "60 - 69"].values[0]
        deaths = df_year.loc[(df_year["gender"]==gender) & (df_year["method"]=="Allcausesofdeath"), "60 - 69"].values[0]
        percent = (N*100)/deaths
        age_60_69.append(percent)

        # 70-79
        N = df_year.loc[(df_year["gender"]==gender) & (df_year["method"]=="Totalsuicides"), "70 - 79"].values[0]
        deaths = df_year.loc[(df_year["gender"]==gender) & (df_year["method"]=="Allcausesofdeath"), "70 - 79"].values[0]
        percent = (N*100)/deaths
        age_70_79.append(percent)

        # 80-89
        N = df_year.loc[(df_year["gender"]==gender) & (df_year["method"]=="Totalsuicides"), "80 - 89"].values[0]
        deaths = df_year.loc[(df_year["gender"]==gender) & (df_year["method"]=="Allcausesofdeath"), "80 - 89"].values[0]
        percent = (N*100)/deaths
        age_80_89.append(percent)

        # 90+
        N = df_year.loc[(df_year["gender"]==gender) & (df_year["method"]=="Totalsuicides"), "90 +"].values[0]
        deaths = df_year.loc[(df_year["gender"]==gender) & (df_year["method"]=="Allcausesofdeath"), "90 +"].values[0]
        percent = (N*100)/deaths
        age_90_plus.append(percent)

    # convert data to df

    data = {
        "0-19": age_0_19, 
        "20-29": age_20_29,
        "30-39": age_30_39,
        "40-49": age_40_49, 
        "50-59": age_50_59,
        "60-69": age_60_69,
        "70-79" :  age_70_79,
        "80-89": age_80_89,
        "90+": age_90_plus
    }
    df = pd.DataFrame(data)
    df = df.melt(var_name='Age', value_name='perc. deaths from Suicide')
    sns.boxplot(x='Age', y='perc. deaths from Suicide', data=df)
    plt.title(f"Percentage of deaths from suicide for different age groups for {gender} from year 2008-2021")
    plt.xlabel('Age Groups')
    plt.ylabel('Percentage of deaths from Suicide')
    plt.show()

def compare_genders(path, years, age_group):
    df = pd.read_csv(path)
    men = []
    women = []
    for year in years:
        df_year = df.loc[df["year"]==year]


        # men
        N = df_year.loc[(df_year["gender"]=="Men") & (df_year["method"]=="Totalsuicides"), age_group].values[0]
        deaths = df_year.loc[(df_year["gender"]=="Men") & (df_year["method"]=="Allcausesofdeath"), age_group].values[0]
        percent = (N*100)/deaths
        men.append(percent)

        # women
        N = df_year.loc[(df_year["gender"]=="Women") & (df_year["method"]=="Totalsuicides"), age_group].values[0]
        deaths = df_year.loc[(df_year["gender"]=="Women") & (df_year["method"]=="Allcausesofdeath"), age_group].values[0]
        percent = (N*100)/deaths
        women.append(percent)

    data = {
        "Men": men,
        "Women": women
    }
    df = pd.DataFrame(data)


    # plotting box plots
    df = df.melt(var_name='Gender', value_name='perc. deaths from Suicide for 20-29 age group')
    sns.boxplot(x='Gender', y='perc. deaths from Suicide for 20-29 age group', data=df)
    plt.title(f"Percentage of deaths from suicide for 20-29 age groups for different genders from year 2008-2021")
    plt.xlabel('Genders')
    plt.ylabel('Perc. deaths from Suicide')
    plt.show()

    # perform t test
    t_stat, p_value = stats.ttest_ind(data["Men"], data["Women"])
    print("T-Statistic:", t_stat)
    print("P-Value:", p_value)


if __name__ == '__main__':
    years = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
    # bar_plot(overview.INPATH, years, "Women")
    # boxplots(overview.INPATH, years, "Men")
    compare_genders(overview.INPATH, years, "20 - 29")