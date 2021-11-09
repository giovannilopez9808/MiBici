import pandas as pd
import calendar


def format_data(data: pd.DataFrame):
    data.index = pd.to_datetime(data["Date"])
    data = data.drop(columns="Date")
    return data


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
