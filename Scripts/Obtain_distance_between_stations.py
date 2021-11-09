from Functions import *

parameters = {"path information": "../Information/",
              "path output": "../Output/",
              "file information": "nomenclatura.csv",
              "file output": "Distance_between.csv"}
# Lectura de las estaciones
stations_data = read_data(parameters["path information"],
                          parameters["file information"])
# Creacion del dataframe que guardara los resultados
stations_distance = create_stations_dataframe(stations_data["id"],
                                              stations_data["id"],
                                              use_float=True)
for index_i in stations_data.index:
    index_j = index_i+1
    id_i = stations_data["id"][index_i]
    lat_i = stations_data["latitude"][index_i]
    lon_i = stations_data["longitude"][index_i]
    while(index_j <= stations_data.index[-1]):
        id_j = stations_data["id"][index_j]
        lat_j = stations_data["latitude"][index_j]
        lon_j = stations_data["longitude"][index_j]
        distance = obtain_distance_bewteen_points(lat_i,
                                                  lon_i,
                                                  lat_j,
                                                  lon_j)
        stations_distance[id_i][id_j] = distance
        stations_distance[id_j][id_i] = distance
        index_j += 1
stations_distance.to_csv("{}{}".format(parameters["path output"],
                                       parameters["file output"]))
