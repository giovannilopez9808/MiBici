from Functions import *
import pandas as pd
import os


def clean_data(data: pd.DataFrame, columns: list):
    drop_columns = data.columns
    drop_columns = drop_columns.drop(columns)
    data = data.drop(columns=drop_columns)
    return data


def create_stations_dataframe(index: list, columns: list):
    data = pd.DataFrame(index=index,
                        columns=columns)
    data.index.names = ["id"]
    data = data.fillna(0)
    return data


parameters = {"path data": "../Data/",
              "path information": "../Information/",
              "file information": "nomenclatura.csv",
              "path output": "../Output/",
              "file output": "Repetition_station.csv",
              "count columns": ["Origen_Id", "Destino_Id"],
              "information columns": ["latitude", "longitude"]}

files = sorted(os.listdir(parameters["path data"]))
stations_data = pd.read_csv("{}{}".format(parameters["path information"],
                                          parameters["file information"]),
                            index_col=0)
stations_data = clean_data(stations_data,
                           parameters["information columns"])
stations_count = create_stations_dataframe(stations_data.index,
                                           parameters["count columns"])
for file in files:
    print("Analizando archivo {}".format(file))
    data = read_data(parameters["path data"],
                     file)
    for id in stations_count.index:
        for column in parameters["count columns"]:
            count = data[data[column] == id][column].count()
            stations_count[column][id] = stations_count[column][id] + count
stations_count.to_csv("{}{}".format(parameters["path output"],
                                    parameters["file output"]))
