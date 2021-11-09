from Map_functions import *
from Functions import *
from pylab import *


def normalize_data(data: pd.DataFrame, columns: list):
    for column in columns:
        max = data[column].max()
        data[column] = data[column]/max
    return data


parameters = {"path map": "../Graphics/",
              "path data": "../Output/",
              "path information": "../Information/",
              "file map": "map.png",
              "file data": "Repetition_station.csv",
              "file coordinates": "coordinates.csv",
              "file information": "nomenclatura.csv",
              "count columns": ["Origen_Id", "Destino_Id"],
              "information columns": ["latitude", "longitude"]}

map = Map_class(parameters["path map"],
                parameters["file map"])
stations_data = read_data(parameters["path information"],
                          parameters["file information"])
count_data = read_data(parameters["path data"],
                       parameters["file data"])
coordinates = np.loadtxt("{}{}".format(parameters["path information"],
                                       parameters["file coordinates"]),
                         delimiter=",")
stations_data = transform_coordenates_to_pixel_location(map,
                                                        coordinates,
                                                        stations_data)
count_data = normalize_data(count_data,
                            parameters["count columns"])
cmap = cm.get_cmap('inferno', 10)
for column in parameters["count columns"]:
    # data = count_data[count_data[column] >= 0.1]
    plt.subplots(figsize=(9, 4))
    plt.axis("off")
    points = plt.scatter(stations_data["longitude"],
                         stations_data["latitude"],
                         alpha=0.8,
                         c=count_data[column],
                         cmap=cmap,
                         vmin=0.1,
                         vmax=1)
    plt.imshow(map.img,
               origin="lower")
    plt.colorbar(points, ticks=np.arange(0, 1.1, 0.1))
    plt.tight_layout()
    graphic_name = "repetition_{}.png".format(column.split("_")[0].lower())
    plt.savefig("{}{}".format(parameters["path map"],
                              graphic_name),
                pad_inches=0,
                dpi=400)
