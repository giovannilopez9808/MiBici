import matplotlib.pyplot as plt
from Functions import *

parameters = {"path data": "../Data/",
              "path information": "../Information/",
              "file information": "nomenclatura.csv"}

info = read_data(parameters["path information"],
                 parameters["file information"])
print("Latitud",
      info["latitude"].min(),
      info["latitude"].max())
print("Longitud",
      info["longitude"].min(),
      info["longitude"].max())
plt.scatter(info["latitude"],
            info["longitude"])
plt.show()
