from Functions import *


def time_format(data: DataFrame, date_column: str) -> DataFrame:
    data.index = pd.to_datetime(data[date_column])
    data = data.drop(columns=date_column)
    return data


def format_data(data: DataFrame, columns: list) -> DataFrame:
    data = data.drop(columns=columns)
    data = data.drop_duplicates()
    return data


parameters = {"path data": "../Data/",
              "path output": "../Output/",
              "file output": "Hourly_mean_time_travel.csv",
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
hourly_count_origin = create_hourly_dataframe(dates)
for file in files:
    print("Analizando archivo {}".format(file))
    data = read_data(parameters["path data"],
                     file)
    data = format_data(data,
                       parameters["useless columns"])
    data = obtain_travel_time(data)
    data = time_format(data,
                       "Inicio_del_viaje")
    hourly_data = data.resample("H").mean()
    del data
    for index in hourly_data.index:
        value = hourly_data["Minutes"][index]
        hour = index.time().hour
        date = index.date()
        hourly_count_origin.loc[date, hour] = value
    del hourly_data
hourly_count_origin.index.names = ["Date"]
hourly_count_origin.to_csv("{}{}".format(parameters["path output"],
                                         parameters["file output"]))
