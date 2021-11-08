import matplotlib.pyplot as plt
from Functions import *
import numpy as np
import matplotlib


def read_image(path: str, file: str):
    img = plt.imread("{}{}".format(path, file))
    img = np.flipud(img)
    return img


def obtain_map_pixel(map: matplotlib.image.AxesImage):
    return [len(map), len(map[1])]


def transform_coordenates_to_pixel_location(map: matplotlib.image.AxesImage, coordinates: np.array, info: pd.DataFrame):
    labels = ["latitude", "longitude"]
    map_pixel = [len(map), len(map[1])]
    initial_point = coordinates[0]
    final_point = coordinates[2]
    for i in range(2):
        label = labels[i]
        pixel = map_pixel[i]
        initial_pos = initial_point[i]
        final_pos = final_point[i]
        proportion = pixel/(final_pos - initial_pos)
        info[label] = (info[label] - initial_pos)*proportion-0.5
    return info


parameters = {"path data": "../Data/",
              "path information": "../Information/",
              "path map": "../Graphics/",
              "file information": "nomenclatura.csv",
              "file coordinates": "coordinates2.csv",
              "photo map": "map2.png"}

info = read_data(parameters["path information"],
                 parameters["file information"])
coordinates = np.loadtxt("{}{}".format(parameters["path information"],
                                       parameters["file coordinates"]),
                         delimiter=",")
print("Latitud",
      info["latitude"].min(),
      info["latitude"].max())
print("Longitud",
      info["longitude"].min(),
      info["longitude"].max())
map = read_image(parameters["path map"],
                 parameters["photo map"])
info = transform_coordenates_to_pixel_location(map, coordinates, info)
plt.scatter(info["longitude"],
            info["latitude"])
plt.imshow(map,
           origin="lower")
plt.show()
