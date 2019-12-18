import names
import pandas as pd
import numpy as np
import random as rand

# SECTION 1
# Creating a list to store random student names
from pandas import DataFrame

num = 100  # Determining the number of students
name_list = []  # Preallocating the list to store names
for i in range(num):
    name_list.append(names.get_full_name())

# Generating a random score array in the range of 0 to 100 for 5 subjects
df_array = [np.array(name_list).transpose()]  # Preallocating the array for the dataframe
subjects = ['Japanese', 'English', 'Mathematics', 'Social_Studies', 'Science']  # List of subjects
for x in subjects:
    score_list = []
    for y in range(num):
        # Generating a list with random number in the range of 0 to 100
        rand_num = rand.random() * 101
        score_list.append(rand_num)
    # Assigning the subject name as the variable name for simplicity
    vars()[x] = np.around(score_list, decimals=1)
    # Appending the random number list to the array for dataframe
    df_array.append(vars()[x])

# Creating pandas dataframe
col_names = ['Student_Name'] + subjects  # Concatenating the list for column names
df: DataFrame = pd.DataFrame(list(zip(name_list, Japanese, English, Mathematics, Social_Studies, Science)), columns=col_names)

# SECTION 2
# Calculating the HENSACHI for all students
df['Total'] = df.loc[:, 'Japanese':'Science'].sum(axis=1)
df['Average'] = df.loc[:, 'Japanese':'Science'].mean(axis=1, numeric_only=True)
df.sort_values(by='Total', inplace=True, ascending=False)
df = df.reset_index(drop=True)

JPN_avg = df['Japanese'].mean(axis=0)
JPN_std = df['Japanese'].std(axis=0)
ENG_avg = df['English'].mean(axis=0)
ENG_std = df['English'].std(axis=0)
MA_avg = df['Mathematics'].mean(axis=0)
MA_std = df['Mathematics'].std(axis=0)
SS_avg = df['Social_Studies'].mean(axis=0)
SS_std = df['Social_Studies'].std(axis=0)
SC_avg = df['Science'].mean(axis=0)
SC_std = df['Science'].std(axis=0)
total_avg = df['Average'].mean(axis=0)
total_std = df['Total'].std(axis=0)
df.loc[-1, 'Student_Name':'Average'] = ['Subject Averages', JPN_avg, ENG_avg, MA_avg, SS_avg, SC_avg, total_avg, None]
df.loc[-2, 'Student_Name':'Average'] = ['Subject Standard Deviations', JPN_std, ENG_std, MA_std, SS_std, SC_std, total_std, None]

new_labels = ['JPN_HENSACHI', 'ENG_HENSACHI', 'MA_HENSACHI', 'SS_HENSACHI', 'SC_HENSACHI', 'SOGO_HENSACHI']
col_names = col_names + ['Total']
ct = 1
for x in new_labels:
    for y in range(num):
        if x != 'SOGO_HENSACHI':
            df.loc[y, x] = 50 + (df.loc[y, col_names[ct]] - df.loc[-1, col_names[ct]]) * 10 / df.loc[-2, col_names[ct]]
        else:
            df.loc[y, x] = df.loc[y, 'JPN_HENSACHI':'SC_HENSACHI'].mean()
    ct += 1
df = df.round(2)
df.to_excel('hensachi_sample.xlsx', sheet_name='Sheet1', engine='xlsxwriter')  # doctest: +SKIP

