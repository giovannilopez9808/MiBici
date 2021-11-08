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


def transform_coordenates_to_pixel_location(map: matplotlib.image.AxesImage,
                                            coordinates: np.array,
                                            info: pd.DataFrame):
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


'''
def obtain_ticks(coordinates: np.array, map_pixel: list, n_grid: int):
    initial_point = coordinates[0]
    inter_point = coordinates[1]
    final_point = coordinates[-1]
    xticks_map = np.linspace(-0.5, map_pixel[0]-0.5, n_grid)
    yticks_map = np.linspace(-0.5, map_pixel[1]-0.5, n_grid)
    xticks = np.linspace(initial_point[0], inter_point[0], n_grid)
    print(xticks)
    yticks = np.linspace(initial_point[1], final_point[1], n_grid)
    return [xticks_map, xticks], [yticks_map, yticks]

def degree_decimal_to_minute_seconds(degrees: np.array):
    degrees_minute = []
    for degree in degrees:
        degree_list = []
        for i in range(3):
            degree_aux = int(degree)
            degree = (degree-degree_aux)*100
            degree_list.append(degree_aux)
        degrees_minute.append("{} {}' {}''".format(degree_list[0],
                                                   degree_list[1],
                                                   degree_list[2]))
    return degrees_minute
'''


parameters = {"path data": "../Data/",
              "path information": "../Information/",
              "path map": "../Graphics/",
              "file information": "nomenclatura.csv",
              "file coordinates": "coordinates.csv",
              "photo map": "map.png",
              "output map": "stations.png"}

info = read_data(parameters["path information"],
                 parameters["file information"])
coordinates = np.loadtxt("{}{}".format(parameters["path information"],
                                       parameters["file coordinates"]),
                         delimiter=",")
map = read_image(parameters["path map"],
                 parameters["photo map"])
map_pixel = obtain_map_pixel(map)
info = transform_coordenates_to_pixel_location(map,
                                               coordinates,
                                               info)
#xticks, yticks = obtain_ticks(coordinates, map_pixel, 5)
plt.scatter(info["longitude"],
            info["latitude"],
            alpha=0.7,
            c="#76c893")
plt.imshow(map,
           origin="lower")
# plt.yticks(xticks[0],
#           xticks[1])
# plt.xticks(yticks[0],
#           yticks[1])
plt.axis("off")
plt.subplots_adjust(left=0,
                    bottom=0.05,
                    right=1,
                    top=0.95)
plt.savefig("{}{}".format(parameters["path map"],
                          parameters["output map"]),
            bbox_inches="tight",
            pad_inches=0,
            dpi=400)
