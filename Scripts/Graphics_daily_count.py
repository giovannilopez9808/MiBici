import matplotlib.pyplot as plt
from Functions import *

parameters = {"path data": "../Output/",
              "file data": "Daily_count.csv"}
# Lectura de los datos
data = pd.read_csv("{}{}".format(parameters["path data"],
                                 parameters["file data"]))
# Formato de los datos
data = format_data(data)
# Calculo del promedio mensual
data = data.resample("MS").mean()
plt.subplots(figsize=(9, 3))
# Ploteo de los datos
plt.scatter(data.index, data["Count"])
plt.tight_layout()
plt.show()
