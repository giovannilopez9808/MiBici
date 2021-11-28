import matplotlib.pyplot as plt
from Functions import *

parameters = {"path output": "../Output/",
              "file data": "Daily_mean_time_travel.csv"}

data = read_data(parameters["path output"],
                 parameters["file data"])
data = format_data(data)
data = data.resample("MS").mean()
plt.plot(data.index, data["Time"],
         marker="o")
plt.show()
