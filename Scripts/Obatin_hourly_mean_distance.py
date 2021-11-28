from Functions import *


def create_hourly_dataframe(index: list) -> DataFrame:
    hours = [hour for hour in range(24)]
    data = pd.DataFrame(index=index,
                        columns=hours)
    data = data.fillna(0.0)
    return data


def time_format(data: DataFrame, date_column: str) -> DataFrame:
    data.index = pd.to_datetime(data[date_column])
    data = data.drop(columns=date_column)
    return data


def clean_useless_data(data: DataFrame, columns: list) -> DataFrame:
    data = data.drop(columns=columns)
    data = data[data["diff"] != 0]
    return data


def format_data(data: DataFrame, columns: list) -> DataFrame:
    data["diff"] = data["Origen_Id"]-data["Destino_Id"]
    data["Distance"] = 0.0
    data.index = pd.to_datetime(data["Inicio_del_viaje"])
    data = clean_useless_data(data, columns)
    data = data.drop_duplicates()
    return data


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
    data = format_data(data,
                       parameters["useless columns"])
    data = fill_distance_data(data,
                              distance_data)
    hourly_data = data.resample("H").mean()
    for index in hourly_data.index:
        value = hourly_data["Distance"][index]
        hour = index.time().hour
        date = index.date()
        hourly_count_origin.loc[date, hour] = value
hourly_count_origin.index.names = ["Date"]
hourly_count_origin.to_csv("{}{}".format(parameters["path output"],
                                         parameters["file output"]))
