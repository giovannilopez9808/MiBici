from Functions import *


parameters = {"path data": "../Data/",
              "path output": "../Output/",
              "file output": "Hourly_mean_distance.csv",
              "file distances": "Distance_between.csv",
              "useless columns": ["Usuario_Id",
                                  "Genero",
                                  "Viaje_Id",
                                  "Año_de_nacimiento"]
              }
files = obtain_filenames(parameters["path data"])
period = obtain_period_from_filenames(files)
dates = obtain_consecutive_dates_from_period(period)
hourly_count_origin = create_hourly_dataframe(dates)
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
    hourly_data = data.resample("H").mean()
    del data, distances
    for index in hourly_data.index:
        value = hourly_data["Distance"][index]
        hour = index.time().hour
        date = index.date()
        hourly_count_origin.loc[date, hour] = value
    del hourly_data
hourly_count_origin.index.names = ["Date"]
hourly_count_origin.to_csv("{}{}".format(parameters["path output"],
                                         parameters["file output"]))
