import pandas
from data_exploration import DataExploration as DE

# read data set
raw_data = pandas.read_csv("./data/train.csv", nrows=10000, index_col=False)
df = raw_data

# let's explore the data
DE.explore_data(raw_data)

# let's see the memory consumption
print("Data consumed %s gb." % (df.memory_usage(index=True, deep=True).sum() / (1024 * 1024)))
