from pandas.core.frame import DataFrame
from datetime import datetime
import pandas as pd
import calendar
import os


def format_data(data: DataFrame) -> DataFrame:
    """ 
    Formato de fecha a la columna "Date" a una base de datos dada
    """
    data.index = pd.to_datetime(data["Date"])
    data = data.drop(columns="Date")
    return data


def read_data(path: str, file: str) -> DataFrame:
    """ 
    Lectura de los datos
    """
    data = pd.read_csv("{}{}".format(path, file))
    return data


def obtain_year_and_month_from_filename(file: str) -> str:
    """
    Obtiene el año y mes del a partir del nombre del archivo
    """
    filename = file.replace(".csv", "")
    filename = filename.split("_")
    year, month = filename
    return [year, month]


def obtain_period_from_filenames(files: list) -> list:
    """
    Obtiene el periodo dado una lista de archivos ordenados.Los archivos contienen la fecha de los datos en su nombre
    """
    # Fecha inicial
    date_initial = files[0]
    # Fecha final
    date_final = files[-1]
    # Fechas
    dates = [date_initial,
             date_final]
    #  Inicializador del periodo
    period = []
    for i in range(2):
        date = dates[i]
        # Obtiene el mes y año a partr del nombre
        year, month = obtain_year_and_month_from_filename(date)
        # Para el limite inferior de toma el dia primero
        day = 1
        if i == 1:
            # Para el limite supeior se toma el ultimo dia del mes
            day = calendar.monthrange(int(year),
                                      int(month))[i]
        #   Formato del dia a dos digitos
        day = str(day).zfill(2)
        # Formato del periodo
        period.append(pd.to_datetime("{}-{}-{}".format(year,
                                                       month,
                                                       day)).date())
    return period


def obtain_next_day(date: datetime) -> datetime:
    """
    Obtiene la fecha siguiente de una fecha
    """
    return date+pd.to_timedelta(1, unit="day")


def obtain_consecutive_dates_from_period(period: list) -> list:
    """
    Obtiene las fechas consecutivas a partir de un periodo dado
    """
    # Primera fecha
    dates = [period[0]]
    while(dates[-1] != period[1]):
        # Obtiene la ultima fecha añadida
        date = dates[-1]
        # Obtiene el dia siguiente
        date = obtain_next_day(date)
        # Añadida a la lista
        dates.append(date)
    return dates


def obtain_filenames(path: str) -> list:
    return sorted(os.listdir(path))
