import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


class Map_class:
    def __init__(self, path: str, file: str):
        self.read_image(path, file)

    def read_image(self, path: str, file: str):
        img = plt.imread("{}{}".format(path, file))
        self.img = np.flipud(img)

    def obtain_map_pixel(self):
        return [len(self.img), len(self.img[1])]


def transform_coordenates_to_pixel_location(map: Map_class,
                                            coordinates: np.array,
                                            info: pd.DataFrame):
    labels = ["latitude", "longitude"]
    map_pixel = map.obtain_map_pixel()
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
