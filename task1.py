import pickle
import pandas as pd
import json
import matplotlib.pyplot as plt

# Unpickling pandas data
pickle_data = open('data.pkl', 'rb').read()
data = pickle.loads(pickle_data)

# loading json data as dict to work with
with open('names.json') as names:
    name_dict = json.load(names)

# initial key value in names.json
names_index = 1
# swap 1's with corresponding values in names.json
for i in range(len(data['task'])):
    if data['task'][i] == 1:
        data['task'][i] = name_dict[str(names_index)]
        # print(i)
    else:
        # check if index is zero to prevent ValueError when we check for previous index
        if i != 0:
            # increment name index to switch to other value to name 1's in task
            if data['task'][i] != data['task'][i - 1]:
                names_index = names_index + 1

# need temporary list to hold all string elements of task data after 1's were switched
temp = []
for i in data['task']:
    if isinstance(i, str):
        temp.append(i)

# show the occurrence in pandas series in descending order
print(pd.Series(temp).value_counts())

# pandas had plot library from matplotlib to plot bar graphs
# here we label x and y axis and plot the occurrence of words
pd.Series(temp).value_counts().plot(xlabel='words', ylabel='occurrence', kind='bar', title='count values of names')
plt.show()
