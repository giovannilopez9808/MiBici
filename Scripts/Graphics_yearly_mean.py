import matplotlib.pyplot as plt
from Functions import *

parameters = {"path data": "../Output/",
              "file data": "Daily_count.csv"}

data = read_data(parameters["path data"],
                 parameters["file data"])
data = format_data(data)
yearly_mean = data.resample("YS").mean()
plt.scatter(yearly_mean.index, yearly_mean["Count"])
plt.show()
