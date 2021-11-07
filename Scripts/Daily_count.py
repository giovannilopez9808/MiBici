import pandas as pd
import calendar
import os


def read_data(path: str, file: str):
    data = pd.read_csv("{}{}".format(path, file))
    return data


def obtain_year_and_month_from_filename(file: str):
    filename = file.replace(".csv", "")
    filename = filename.split("_")
    year, month = filename
    return year, month


def obtain_period_from_filenames(files: list):
    date_initial = files[0]
    date_final = files[-1]
    dates = [date_initial,
             date_final]
    period = []
    for i in range(2):
        date = dates[i]
        year, month = obtain_year_and_month_from_filename(date)
        day = 1
        if i == 1:
            day = calendar.monthrange(int(year),
                                      int(month))[i]
        day = str(day).zfill(2)
        period.append(pd.to_datetime("{}-{}-{}".format(year,
                                                       month,
                                                       day)).date())
    return period


def obtain_consecutive_dates_from_period(period: list):
    dates = [period[0]]
    while(dates[-1] != period[1]):
        date = dates[-1]
        date = date+pd.to_timedelta(1, unit="day")
        dates.append(date)
    return dates


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
