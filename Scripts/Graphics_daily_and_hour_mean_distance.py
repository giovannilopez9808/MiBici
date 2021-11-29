import matplotlib.pyplot as plt
from Functions import *
from pylab import *


def set_day_of_the_week(data: DataFrame, parameters: dict) -> DataFrame:
    data["Day"] = None
    for index in data.index:
        date = data["Date"][index]
        day = date.strftime("%A")
        day_number = parameters["days"][day]
        data.loc[index, "Day"] = day_number
    return data


parameters = {"path data": "../Output/",
              "file data": "Hourly_mean_distance.csv",
              "path graphics": "../Graphics/",
              "file graphics": "daily_and_hour_mean_distance.png",
              "days": {"lunes": "1",
                       "martes": "2",
                       "miércoles": "3",
                       "jueves": "4",
                       "viernes": "5",
                       "sábado": "6",
                       "domingo": "7"}}

data = read_data(parameters["path data"],
                 parameters["file data"])
data["Date"] = pd.to_datetime(data["Date"])
set_day_of_the_week(data,
                    parameters)
data_mean = data.groupby("Day").mean()
data_mean = data_mean.sort_index()
xticks = np.arange(-0.5, 23.5-6+2, 2)
yticks = np.linspace(-0.5, 6.5, 8)
yticks = np.delete(yticks, -1)
xlabels = xticks+0.5+6
xlabels = [int(xlabel) for xlabel in xlabels]
data_mean = data_mean.drop(columns=[str(i) for i in range(6)])
data_mean = data_mean.drop(columns="23")
data_mean = np.array(data_mean)
cmap = cm.get_cmap('Greens', 8)
plt.xticks(xticks,
           xlabels)
plt.yticks(yticks+0.5,
           parameters["days"])
plt.xlabel("Hora local (h)")
plt.grid(ls="--",
         color="#000000",
         alpha=0.5,
         lw=1.5,
         axis="x")
for ytick in yticks:
    plt.plot([xticks[0], 16.5],
             [ytick, ytick],
             ls="--",
             color="#000000",
             alpha=0.5,
             lw=1.5)
print(np.min(data_mean))
print(np.max(data_mean))
plt.imshow(data_mean,
           origin="lower",
           cmap=cmap,
           vmin=1.2,
           vmax=1.6,
           aspect='auto')
plt.tight_layout()
cbar = plt.colorbar(ticks=np.round(np.linspace(1.2, 1.6, 9), 2))
cbar.set_label("Promedio de distancia recorrida (km)",
               rotation=-90,
               labelpad=15)
plt.savefig("{}{}".format(parameters["path graphics"],
                          parameters["file graphics"]),
            dpi=400)
