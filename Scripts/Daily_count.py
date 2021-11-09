from Functions import *
import pandas as pd
import os


def create_daily_dataframe(index: list):
    data = pd.DataFrame(index=index,
                        columns=["Count"])
    data.index.names = ["Date"]
    data = data.fillna(0)
    return data


parameters = {"path data": "../Data/",
              "path output": "../Output/",
              "useless columns": ["Usuario_Id",
                                  "Genero",
                                  "Año_de_nacimiento",
                                  "Inicio_del_viaje",
                                  "Fin_del_viaje",
                                  "Origen_Id",
                                  "Destino_Id"]}
files = sorted(os.listdir(parameters["path data"]))
period = obtain_period_from_filenames(files)
dates = obtain_consecutive_dates_from_period(period)
daily_count = create_daily_dataframe(dates)
for file in files:
    print("Analizando archivo {}".format(file))
    data = read_data(parameters["path data"],
                     file)
    data.index = pd.to_datetime(data["Inicio_del_viaje"])
    data = data.drop(columns=parameters["useless columns"])
    data = data.resample("D").count()
    for index in data.index:
        date = (data["Viaje_Id"][index])
        daily_count["Count"][index.date()] = date
daily_count.to_csv("{}Daily_count.csv".format(parameters["path output"]))
