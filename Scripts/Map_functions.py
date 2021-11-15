from pandas.core.frame import DataFrame
import matplotlib.pyplot as plt
import numpy as np


class Map_class:
    """
    Clase que contiene la lectura y calculo de las propiedades de un mapa dado
    """

    def __init__(self, path: str, file: str) -> None:
        # Lectura de la imagen
        self.read_image(path, file)
        # Calculo de los limites del mapa
        self.map_pixel = self.obtain_map_pixel()

    def read_image(self, path: str, file: str) -> None:
        """
        Lectura de la imagen. Realiza una reflexion vertical
        """
        # Lecuta de la imagen
        img = plt.imread("{}{}".format(path, file))
        # Reflexion vertical
        self.img = np.flipud(img)

    def obtain_map_pixel(self) -> list:
        return [len(self.img), len(self.img[1])]


def transform_coordinates_to_pixel_location(map: Map_class,
                                            coordinates: np.array,
                                            info: DataFrame) -> DataFrame:
    """
    Transformacion de unas coordenadas dadas hacia el espacio de pixeles
    """
    # Labels de las columnas de datos
    labels = ["latitude", "longitude"]
    # Obtiene el limite del mapa en pixeles
    map_pixel = map.obtain_map_pixel()
    # Coordenada inicial
    initial_point = coordinates[0]
    # Coordenada final
    final_point = coordinates[2]
    for i in range(2):
        label = labels[i]
        pixel = map_pixel[i]
        # Posicion inicial
        initial_pos = initial_point[i]
        # Posicion final
        final_pos = final_point[i]
        # Proprocion pixel/coordenadas
        proportion = pixel/(final_pos - initial_pos)
        # Transformacion de las coordenadas
        info[label] = (info[label] - initial_pos)*proportion-0.5
    return info
