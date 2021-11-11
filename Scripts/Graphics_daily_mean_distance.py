import matplotlib.pyplot as plt
from Functions import *

parameters = {"path output": "../Output/",
              "file data": "Daily_mean_distance.csv"}

data = read_data(parameters["path output"],
                 parameters["file data"])
data = format_data(data)
plt.plot(data.index, data["Mean distance"],
         marker="o")
plt.show()
