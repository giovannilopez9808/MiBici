from Functions import *


parameters = {"path output": "../Output/",
              "path data": "../Data/",
              "file output": "Daily_mean_time_travel.csv",
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
daily_data_output = create_daily_dataframe(dates,
                                           header="Time",
                                           use_float=True)
for file in files:
    print("Analizando archivo {}".format(file))
    data = read_data(parameters["path data"],
                     file)
    times = time_algorithm(data,
                           parameters["useless columns"])
    data = times.data
    daily_data = data.resample("D").mean()
    del data, times
    for date in daily_data.index:
        index = date.date()
        value = daily_data["Minutes"][date]
        daily_data_output.loc[index, "Time"] = value
    del daily_data
daily_data_output.to_csv("{}{}".format(parameters["path output"],
                                       parameters["file output"]))
