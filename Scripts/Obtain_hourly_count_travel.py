from Functions import *


def create_hourly_dataframe(index: list) -> DataFrame:
    hours = [hour for hour in range(24)]
    data = pd.DataFrame(index=index,
                        columns=hours)
    data = data.fillna(0.0)
    return data


def format_data(data: DataFrame, columns: list, date_column: str) -> DataFrame:
    data.index = pd.to_datetime(data[date_column])
    data = data.drop(columns=columns)
    data = data.drop_duplicates()
    return data


parameters = {"path data": "../Data/",
              "path output": "../Output/",
              "file output": "Hourly_count_travel.csv",
              "useless columns": ["Usuario_Id",
                                  "Genero",
                                  "Viaje_Id",
                                  "Año_de_nacimiento",
                                  "Inicio_del_viaje",
                                  "Fin_del_viaje"]}

files = obtain_filenames(parameters["path data"])
period = obtain_period_from_filenames(files)
dates = obtain_consecutive_dates_from_period(period)
hourly_count_origin = create_hourly_dataframe(dates)
for file in files:
    print("Analizando archivo {}".format(file))
    data = read_data(parameters["path data"],
                     file)
    data = format_data(data,
                       parameters["useless columns"],
                       "Inicio_del_viaje")
    hourly_data = data.resample("H").count()
    for index in hourly_data.index:
        value = hourly_data["Origen_Id"][index]
        hour = index.time().hour
        date = index.date()
        hourly_count_origin[hour][date] = value
hourly_count_origin.index.names = ["Date"]
hourly_count_origin.to_csv("{}{}".format(parameters["path output"],
                                         parameters["file output"]))
