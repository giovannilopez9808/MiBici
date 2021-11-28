import matplotlib.pyplot as plt
from Functions import *

parameters = {"path data": "../Output/",
              "path graphics": "../Graphics/",
              "file data": "Daily_count_travel.csv",
              "file graphics": "monthly_mean_count_travel.png",
              "file output": "Monthly_mean_count_travel.csv"}
# Lectura de los datos
data = pd.read_csv("{}{}".format(parameters["path data"],
                                 parameters["file data"]))
# Formato de los datos
data = format_data(data)
# Calculo del promedio mensual
data = data.resample("MS").mean()
plt.subplots(figsize=(9, 3))
plt.xlim(pd.to_datetime("2015-01-01"),
         pd.to_datetime("2019-01-01"))
plt.ylim(0, 12000)
plt.ylabel("Número de viajes promedio")
# Ploteo de los datos
plt.scatter(data.index, data["Count"])
plt.tight_layout()
plt.savefig("{}{}".format(parameters["path graphics"],
                          parameters["file graphics"]),
            dpi=400)
data.to_csv("{}{}".format(parameters["path data"],
                          parameters["file output"]))
