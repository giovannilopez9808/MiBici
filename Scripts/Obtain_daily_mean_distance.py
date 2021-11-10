from numpy import SHIFT_DIVIDEBYZERO
from Functions import *
pd.options.mode.chained_assignment = None


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


def fill_distance_data(data: DataFrame, distance_data: DataFrame) -> DataFrame:
    for index in data.index:
        index_list_i = np.array(data["Origen_Id"][index])
        index_list_j = np.array(data["Destino_Id"][index])
        size = np.size(index_list_i)
        if size > 1:
            for pos in range(size):
                index_i = index_list_i[pos]
                index_j = index_list_j[pos]
                distance = distance_data[str(index_i)][index_j]
                data["Distance"][index] = distance
        else:
            index_i = index_list_i
            index_j = index_list_j
            distance = distance_data[str(index_i)][index_j]
            data["Distance"][index] = distance
    data = data.drop(columns=["Origen_Id", "Destino_Id", "diff"])
    return data


def filter_data(data: DataFrame, stations: list) -> DataFrame:
    stations = list(stations)
    labels = ["Origen_Id", "Destino_Id"]
    for index in data.index:
        labels_id_i = np.array(data[labels[0]][index])
        labels_id_j = np.array(data[labels[1]][index])
        size = np.size(labels_id_i)
        if size > 1:
            for i in range(size):
                if (not(labels_id_i[i] in stations) or not(labels_id_j[i] in stations)):
                    data = data.drop(index)
        else:
            if (not(labels_id_i in stations) or not(labels_id_j in stations)):
                data = data.drop(index)

    return data


parameters = {"path output": "../Output/",
              "path data": "../Data/",
              "path information": "../Information/",
              "file distances": "Distance_between.csv",
              "file output": "Daily_mean_distance.csv",
              "useless columns": ["Usuario_Id",
                                  "Genero",
                                  "Viaje_Id",
                                  "Año_de_nacimiento",
                                  "Inicio_del_viaje",
                                  "Fin_del_viaje"]
              }

files = obtain_filenames(parameters["path data"])
period = obtain_period_from_filenames(files)
dates = obtain_consecutive_dates_from_period(period)
daily_data_output = create_daily_dataframe(dates,
                                           header="Mean distance",
                                           use_float=True)
distance_data = read_data(parameters["path output"],
                          parameters["file distances"],
                          use_index=True)
for file in files:
    print("Analizando archivo {}".format(file))
    data = read_data(parameters["path data"],
                     file)
    data = format_data(data,
                       parameters["useless columns"])
    data = filter_data(data,
                       distance_data.index)
    data = fill_distance_data(data,
                              distance_data)

    daily_data = data.resample("D").mean()
    for date in daily_data.index:
        index = date.date()
        daily_data_output["Mean distance"][index] = daily_data["Distance"][date]
daily_data_output.to_csv("{}{}".format(parameters["path output"],
                                       parameters["file output"]))
