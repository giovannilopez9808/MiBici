from Functions import *

parameters = {"path data": "../Data/",
              "path output": "../Output/",
              "file mean output": "Hourly_mean_time_travel.csv",
              "file var output": "Hourly_var_time_travel.csv",
              "useless columns": ["Usuario_Id",
                                  "Genero",
                                  "Viaje_Id",
                                  "Origen_Id",
                                  "Destino_Id",
                                  "Año_de_nacimiento"]
              }
files = obtain_filenames(parameters["path data"])
period = obtain_period_from_filenames(files)
dates = obtain_consecutive_dates_from_period(period)
hourly_mean = create_hourly_dataframe(dates)
hourly_var = create_hourly_dataframe(dates)
for file in files:
    print("Analizando archivo {}".format(file))
    data = read_data(parameters["path data"],
                     file)
    times = time_algorithm(data,
                           parameters["useless columns"])
    data = times.data
    hourly_mean_data = data.resample("H").mean()
    hourly_var_data = data.resample("H").var()
    del data, times
    for index in hourly_mean_data.index:
        value = hourly_mean_data["Minutes"][index]
        hour = index.time().hour
        date = index.date()
        hourly_mean.loc[date, hour] = value
        value = hourly_var_data["Minutes"][index]
        hourly_var.loc[date, hour] = value
    del hourly_mean_data
hourly_mean.index.names = ["Date"]
hourly_var.index.names = ["Date"]
hourly_mean.to_csv("{}{}".format(parameters["path output"],
                                 parameters["file mean output"]))
hourly_var.to_csv("{}{}".format(parameters["path output"],
                                parameters["file var output"]))
