from Functions import *

parameters = {"path output": "../Output/",
              "path data": "../Data/",
              "path information": "../Information/",
              "file distances": "Distance_between.csv",
              "file output": "Daily_mean_distance.csv",
              "useless columns": ["Usuario_Id",
                                  "Genero",
                                  "Viaje_Id",
                                  "Año_de_nacimiento",
                                  "Inicio_del_viaje",
                                  "Fin_del_viaje"]
              }

files = obtain_filenames(parameters["path data"])
period = obtain_period_from_filenames(files)
dates = obtain_consecutive_dates_from_period(period)
daily_data_output = create_daily_dataframe(dates,
                                           header="Mean distance",
                                           use_float=True)
distance_data = read_data(parameters["path output"],
                          parameters["file distances"],
                          use_index=True)
for file in files:
    print("Analizando archivo {}".format(file))
    data = read_data(parameters["path data"],
                     file)
    distances = distance_algorithm(data,
                                   parameters["useless columns"],
                                   distance_data,
                                   distance_data.index)
    data = distances.data
    daily_data = data.resample("D").mean()
    del data
    for date in daily_data.index:
        index = date.date()
        value = daily_data["Distance"][date]
        daily_data_output.loc[index, "Mean distance"] = value
    del daily_data
daily_data_output.to_csv("{}{}".format(parameters["path output"],
                                       parameters["file output"]))
