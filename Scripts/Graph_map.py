from Map_functions import *
from Functions import *

parameters = {"path data": "../Data/",
              "path information": "../Information/",
              "path map": "../Graphics/",
              "file information": "nomenclatura.csv",
              "file coordinates": "coordinates.csv",
              "photo map": "map.png",
              "output map": "stations.png"}

# Obtiene los datos de las estaciones
stations_data = read_data(parameters["path information"],
                          parameters["file information"])
#   Obtiene la lista de coordenadas de los vertices del mapa
coordinates = np.loadtxt("{}{}".format(parameters["path information"],
                                       parameters["file coordinates"]),
                         delimiter=",")
#  Lectura el mapa dentro de una clase
map = Map_class(parameters["path map"],
                parameters["photo map"])
# Transforma las coordenadas de las estaciones a pixeles
stations_data = transform_coordinates_to_pixel_location(map,
                                                        coordinates,
                                                        stations_data)
# Borrado de los ticks
plt.axis("off")
# Plot de las estaciones
plt.scatter(stations_data["longitude"],
            stations_data["latitude"],
            alpha=0.7,
            c="#76c893",
            s=10)
# Plot del mapa
plt.imshow(map.img,
           origin="lower")
# Ajuste del plot
plt.subplots_adjust(left=0,
                    bottom=0.05,
                    right=1,
                    top=0.95)
# Guardado del plot
plt.savefig("{}{}".format(parameters["path map"],
                          parameters["output map"]),
            bbox_inches="tight",
            pad_inches=0,
            dpi=400)
