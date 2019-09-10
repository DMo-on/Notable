
from numpy import random
from random import randint
from Comrad import Comrad
import torch
import pandas as pd
import matplotlib.pyplot as plt

file = pd.read_excel("../datasets/SportsArticles/features.xlsx")
file.dropna()
inputs = file


from pandas.plotting import scatter_matrix

fig, ax = plt.subplots(figsize=(12,12))
scatter_matrix(inputs, alpha=1, ax=ax)

fig, ax = plt.subplots()

# scatter the sepal_length against the sepal_width
ax.scatter(inputs['exclamationmarks'], inputs["Label"])
# set a title and labels
ax.set_title('Dataset')
ax.set_xlabel('exclamationmarks')
ax.set_ylabel('Label')

# create figure and axis
fig, ax = plt.subplots()
# plot histogram
ax.hist(inputs['Label'])
# set title and labels
ax.set_title('Répartition')
ax.set_xlabel('Label')
ax.set_ylabel('Frequency')

inputs.drop(['Label'], axis=1).plot.line(title='Dataset')




inputs.groupby("questionmarks").price.mean().sort_values(ascending=False)[:5].plot.bar()