import pandas
from data_exploration import DataExploration as DE

# read data set
raw_data = pandas.read_csv("./data/train.csv", nrows=10000, index_col=False)
df = raw_data
# have a glimpse of the data
print(raw_data.head(5))

# let's explore the data
DE.explore_data(raw_data)
