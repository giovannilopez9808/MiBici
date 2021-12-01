import matplotlib.pyplot as plt
from Functions import *

parameters = {"path data": "../Output/",
              "path graphics": "../Graphics/",
              "file data": "Daily_distance.csv",
              "file monthly output": "Monthly_distance.csv",
              "file yearly output": "Yearly_distance.csv"}
# Lectura de los datos
data = pd.read_csv("{}{}".format(parameters["path data"],
                                 parameters["file data"]))
# Formato de los datos
data = format_data(data)
# Calculo del promedio mensual
monthly_mean = data.resample("MS").mean()
yearly_mean = data.resample("Y").mean()
monthly_mean.to_csv("{}{}".format(parameters["path data"],
                                  parameters["file monthly output"]))
yearly_mean.to_csv("{}{}".format(parameters["path data"],
                                 parameters["file yearly output"]))
