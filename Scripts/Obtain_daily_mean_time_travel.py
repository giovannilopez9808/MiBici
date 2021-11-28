from Functions import *
pd.options.mode.chained_assignment = None


def clean_useless_data(data: DataFrame, columns: list) -> DataFrame:
    data = data.drop(columns=columns)
    # data = data[data["diff"] != 0]
    return data


def format_data(data: DataFrame, columns: list) -> DataFrame:
    data["diff"] = data["Origen_Id"]-data["Destino_Id"]
    data["Distance"] = 0.0
    data.index = pd.to_datetime(data["Inicio_del_viaje"])
    data = clean_useless_data(data, columns)
    data = data.drop_duplicates()
    return data


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
    data = format_data(data,
                       parameters["useless columns"])
    data = obtain_travel_time(data)
    daily_data = data.resample("D").mean()
    for date in daily_data.index:
        index = date.date()
        value = daily_data["Minutes"][date]
        daily_data_output["Time"][index] = value
daily_data_output.to_csv("{}{}".format(parameters["path output"],
                                       parameters["file output"]))
