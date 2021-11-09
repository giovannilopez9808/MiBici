import matplotlib.pyplot as plt
from Functions import *

parameters = {"path data": "../Output/",
              "file data": "Daily_count.csv"}
# Lectura de los datos
data = read_data(parameters["path data"],
                 parameters["file data"])
#  Formato de fecha en los datos
data = format_data(data)
# Obtiene el promedio anual
yearly_mean = data.resample("YS").mean()
# Ploteo de los datos
plt.scatter(yearly_mean.index, yearly_mean["Count"])
plt.show()
