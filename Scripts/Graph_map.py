from Map_functions import *
from Functions import *

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
map = Map_class(parameters["path map"],
                parameters["photo map"])
map_pixel = map.obtain_map_pixel()
info = transform_coordenates_to_pixel_location(map,
                                               coordinates,
                                               info)
plt.axis("off")
plt.scatter(info["longitude"],
            info["latitude"],
            alpha=0.7,
            c="#76c893")
plt.imshow(map.img,
           origin="lower")
plt.subplots_adjust(left=0,
                    bottom=0.05,
                    right=1,
                    top=0.95)
plt.savefig("{}{}".format(parameters["path map"],
                          parameters["output map"]),
            bbox_inches="tight",
            pad_inches=0,
            dpi=400)
