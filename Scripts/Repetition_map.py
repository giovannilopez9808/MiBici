from Functions import *


def clean_data(data: DataFrame, columns: list) -> DataFrame:
    """
    Realiza una limpieza a las columnas que no seran utilizadas en los datos
    """
    drop_columns = data.columns
    drop_columns = drop_columns.drop(columns)
    data = data.drop(columns=drop_columns)
    return data


def create_stations_dataframe(index: list, columns: list) -> DataFrame:
    """
    Creacion de un dataframe dadas un indice y columnas
    """
    data = pd.DataFrame(index=index,
                        columns=columns)
    # Nombre del indice
    data.index.names = ["id"]
    # Inicializacion de los datos
    data = data.fillna(0)
    return data


parameters = {"path data": "../Data/",
              "path information": "../Information/",
              "file information": "nomenclatura.csv",
              "path output": "../Output/",
              "file output": "Repetition_station.csv",
              "count columns": ["Origen_Id", "Destino_Id"],
              "information columns": ["latitude", "longitude"]}

# Obtiene el nombre de los archivos de datos
files = obtain_filenames(parameters["path data"])
stations_data = pd.read_csv("{}{}".format(parameters["path information"],
                                          parameters["file information"]),
                            index_col=0)
# Realiza la eliminacion de las columnas de datos que no sera usadas
stations_data = clean_data(stations_data,
                           parameters["information columns"])
# Realiza la creacion del dataframe que guardara los resultados
stations_count = create_stations_dataframe(stations_data.index,
                                           parameters["count columns"])
for file in files:
    print("Analizando archivo {}".format(file))
    # Lectura de los datos
    data = read_data(parameters["path data"],
                     file)
    for id in stations_count.index:
        for column in parameters["count columns"]:
            # Conteo de datos para cada estacion
            count = data[data[column] == id][column].count()
            # Suma de los conteos
            stations_count[column][id] = stations_count[column][id] + count
# Guardado de los resultados
stations_count.to_csv("{}{}".format(parameters["path output"],
                                    parameters["file output"]))
