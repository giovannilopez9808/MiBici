from pandas.core.frame import DataFrame
from datetime import datetime
import pandas as pd
import numpy as np
import calendar
import os


def format_data(data: DataFrame) -> DataFrame:
    """ 
    Formato de fecha a la columna "Date" a una base de datos dada
    """
    data.index = pd.to_datetime(data["Date"])
    data = data.drop(columns="Date")
    return data


def read_data(path: str, file: str, use_index=False) -> DataFrame:
    """ 
    Lectura de los datos
    """
    if use_index:
        data = pd.read_csv("{}{}".format(path, file),
                           index_col=0)
    else:
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


def create_daily_dataframe(index: list, header: str, use_float=False) -> DataFrame:
    """ 
    Crea un dataframe dado un indice y con una columna de titulo count
    """
    data = pd.DataFrame(index=index,
                        columns=[header])
    # Header del index, este aparecera al momento de guardar el documento
    data.index.names = ["Date"]
    # Inicializacion del conteo
    if(use_float):
        data = data.fillna(0.0)
    else:
        data = data.fillna(0)
    return data


def create_stations_dataframe(index: list, columns: list, use_float=False) -> DataFrame:
    """
    Creacion de un dataframe dadas un indice y columnas
    """
    data = pd.DataFrame(index=index,
                        columns=columns)
    # Nombre del indice
    data.index.names = ["id"]
    # Inicializacion de los datos
    if(use_float):
        data = data.fillna(0.0)
    else:
        data = data.fillna(0)
    return data


def obtain_distance_bewteen_points(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    rad = np.pi/180
    dlat = lat2-lat1
    dlon = lon2-lon1
    R = 6372.795477598
    a = (np.sin(rad*dlat/2))**2 + np.cos(rad*lat1) * \
        np.cos(rad*lat2)*(np.sin(rad*dlon/2))**2
    distancia = 2*R*np.arcsin(np.sqrt(a))
    return distancia


def obtain_filenames(path: str) -> list:
    return sorted(os.listdir(path))


def obtain_travel_time(data: DataFrame) -> DataFrame:
    data["Inicio_del_viaje"] = pd.to_datetime(data["Inicio_del_viaje"])
    data["Fin_del_viaje"] = pd.to_datetime(data["Fin_del_viaje"])
    data["Time"] = data["Fin_del_viaje"]-data["Inicio_del_viaje"]
    data["Minutes"] = data["Time"].apply(lambda x: x.total_seconds()/60)
    data = data.drop(columns="Time")
    return data


def fill_distance_data(data: DataFrame, distance_data: DataFrame) -> DataFrame:
    for index in data.index:
        index_list_i = np.array(data["Origen_Id"][index])
        index_list_j = np.array(data["Destino_Id"][index])
        size = np.size(index_list_i)
        if size > 1:
            distance = 0
            for pos in range(size):
                index_i = index_list_i[pos]
                index_j = index_list_j[pos]
                distance += distance_data[str(index_i)][index_j]
            data.loc[index, "Distance"] = distance / size
        else:
            index_i = index_list_i
            index_j = index_list_j
            distance = distance_data[str(index_i)][index_j]
            data.loc[index, "Distance"] = distance
    data = data.drop(columns=["Origen_Id", "Destino_Id", "diff"])
    return data
