import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("C:/cygwin64/home/OrangE/IBI1_2022-23/Practical7")
covid_data = pd.read_csv("full_data.csv")

print(covid_data.iloc[2:1000:100, :])  # code for showing the second column from every 100th row from the first 1000
# rows

i = 1
boolean_list1 = [False]
while i <= 7995:  # create a Boolean
    a = covid_data.loc[i, "location"]
    boolean_list1.append(a == "Afghanistan")
    i = i + 1
print(covid_data.iloc[boolean_list1, 4])  # use a Boolean to show “total cases” for rows corresponding to Afghanistan

o = 1  # way1: use a Boolean
boolean_list2 = [False]
while o <= 7995:
    b = covid_data.loc[o, "date"]
    boolean_list2.append(b == "2020-03-31")
    o = o + 1
data1 = covid_data.loc[boolean_list2, ['new_cases', 'new_deaths']]
data2 = covid_data.loc[covid_data['date'] == '2020-03-31', ['new_cases', 'new_deaths']]  # way2 use loc to search
# data1 and data2 are the same and there are two ways of find the data of specific date

print("mean number of new cases on 31 March 2020 is", np.mean(data2['new_cases']))
print("mean number of new deaths on 31 March 2020 is", np.mean(data2['new_deaths']))
# computed the mean number of new cases and new deaths on 31 March 2020

fig, ax = plt.subplots(2, 2, figsize=(16, 8))

c = data2['new_cases'].to_numpy()
d = data2['new_deaths'].to_numpy()  # change data format
ax[0, 0].boxplot(c), ax[0, 1].boxplot(d)  # create boxplot of new cases and new deaths on 31 March 2020
ax[0, 0].set_xlabel('New Cases'), ax[0, 0].set_ylabel('Number of Cases')
ax[0, 0].set_title('Boxplot of New Cases on 2020-03-31')
ax[0, 1].set_xlabel('New Deaths'), ax[0, 1].set_ylabel('Number of Deaths')
ax[0, 1].set_title('Boxplot of New Deaths on 2020-03-31')

grouped_data = covid_data.groupby("date").sum().reset_index()  # create a new dataframe by groupby and remove the index
world_dates = grouped_data.loc[:, "date"]
world_new_cases = grouped_data.loc[:, "new_cases"]
world_new_deaths = grouped_data.loc[:, "new_deaths"]
ax[1, 0].plot(world_dates, world_new_cases, 'ro')
ax[1, 0].plot(world_dates, world_new_deaths, 'bo')  # plot both new cases and new deaths worldwide over time
ax[1, 0].set_xticks(world_dates.iloc[0:len(world_dates):2])
ax[1, 0].set_xticklabels(world_dates.iloc[0:len(world_dates):2], rotation=-90, fontsize=5)
ax[1, 0].set_xlabel('Date'), ax[1, 0].set_ylabel('Number of Cases/Deaths')
ax[1, 0].set_title('Global Daily New Cases and New Deaths')
ax[1, 1].remove()
plt.tight_layout()
plt.show()

# code for question.txt
us_data = covid_data[covid_data['location'] == 'United States']
uk_data = covid_data[covid_data['location'] == 'United Kingdom']
us_proportion = np.sum(us_data['total_deaths']) / np.sum(us_data['total_cases'])
uk_proportion = np.sum(uk_data['total_deaths']) / np.sum(uk_data['total_cases'])
print('Proportion of cases died in the United Kingdom: {:.2%}'.format(uk_proportion))
print('Proportion of cases died in the United States: {:.2%}'.format(us_proportion))
