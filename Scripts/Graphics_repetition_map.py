from Map_functions import *
from Functions import *
from pylab import *


def normalize_data(data: DataFrame, columns: list) -> DataFrame:
    """
    Normalizacion de los datos entre 0 y 1
    """
    for column in columns:
        total = data[column].sum()
        data[column] = data[column]/total
    return data


def filter_data(data: DataFrame, column: str) -> DataFrame:
    """ 
    Realiza un filtrado de datos a partir de su porcentaje
    """
    data = data[data[column] >= 0.1]
    return data


def plot(stations_data: DataFrame, data: DataFrame, column: str, path: str, graphic_name: str, limits=False) -> None:
    """ 
    Realiza el ploteo del uso de las estaciones en un mapa, si se quiere realzar un zoom en la zona de interes debera dar un True en la variable limits.
    """
    plt.subplots(figsize=(9, 5))
    # Si se quiere analizar la zona de interes
    if(limits):
        # data = filter_data(data, column)
        plt.xlim(170*4, 340*4)
        plt.ylim(150*4, 280*4)
    plt.axis("off")
    # Realiza el ploeto de los puntos con su color dependiento de su porcentaje de uso
    cmap = cm.get_cmap('inferno', 6)
    s = 5
    if "zoom" in graphic_name:
        s = 20
    points = plt.scatter(stations_data["longitude"][data.index],
                         stations_data["latitude"][data.index],
                         alpha=0.85,
                         s=s,
                         c=np.round(data[column], 3),
                         cmap=cmap)
    #  Impresion de los mapas
    plt.imshow(map.img,
               origin="lower")
    # Impresion del colorbar
    cbar = plt.colorbar(points,
                        ticks=np.round(np.linspace(0, 0.024, 7), 3))
    cbar.set_label("Distribución de uso de las estaciones",
                   rotation=-90,
                   fontsize=13,
                   labelpad=20)
    plt.tight_layout()
    # Guardado de la grafica
    plt.savefig("{}{}".format(path,
                              graphic_name),
                pad_inches=0,
                dpi=400)


parameters = {"path map": "../Graphics/",
              "path data": "../Output/",
              "path information": "../Information/",
              "file map": "map.jpg",
              "file data": "Repetition_station.csv",
              "file coordinates": "coordinates.csv",
              "file information": "nomenclatura.csv",
              "count columns": ["Origen_Id"],
              "information columns": ["latitude", "longitude"]}
# Lectura del mapa en una clase
map = Map_class(parameters["path map"],
                parameters["file map"])
# Lectura de los datos de las estaciones
stations_data = read_data(parameters["path information"],
                          parameters["file information"])
# Lectura del conteo de uso de las estaciones
count_data = read_data(parameters["path data"],
                       parameters["file data"])
# Lectura de las coordenadas del vertice del mapa
coordinates = np.loadtxt("{}{}".format(parameters["path information"],
                                       parameters["file coordinates"]),
                         delimiter=",")
# Transforma las coordenadas a el mapa de pixeles
stations_data = transform_coordinates_to_pixel_location(map,
                                                        coordinates,
                                                        stations_data)
# Normalizacion del conteo de uso
count_data = normalize_data(count_data,
                            parameters["count columns"])
# Definicion del colormap
for column in parameters["count columns"]:
    # Nombre de la grafica sin zoom
    graphic_name = "repetition_{}.png".format(
        column.split("_")[0].lower())
    plot(stations_data,
         count_data,
         column,
         parameters["path map"],
         graphic_name)
    #  Nombre de la grafica con zoom
    graphic_name = "repetition_{}_zoom.png".format(
        column.split("_")[0].lower())
    plot(stations_data,
         count_data,
         column,
         parameters["path map"],
         graphic_name,
         limits=True)
