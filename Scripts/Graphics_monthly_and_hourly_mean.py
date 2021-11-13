import matplotlib.pyplot as plt
from Functions import *


parameters = {"path data": "../Output/",
              "file data": "Hourly_count.csv"}

data = read_data(parameters["path data"],
                 parameters["file data"])
data["Date"] = pd.to_datetime(data["Date"])
data["Date"] = data["Date"].apply(lambda x: x.replace(year=2016))
data.index = pd.to_datetime(data["Date"])
data_mean = data.resample("MS").mean()
xticks = np.arange(0.5, 23.5-6+2, 2)
yticks = np.linspace(0.5, 11.5, 13)
yticks = np.delete(yticks, 12)
xlabels = xticks-0.5+6
xlabels = [int(xlabel) for xlabel in xlabels]
ylabels = ["Ene", "Feb", "Mar", "Abril", "May",
           "Jun", "Jul", "Ago", "Sept", "Oct", "Nov", "Dec"]
data_mean = data_mean.drop(columns=[str(i) for i in range(6)])
data_mean = data_mean.drop(columns="23")
data_mean = np.array(data_mean)
plt.xticks(xticks,
           xlabels)
plt.yticks(yticks,
           ylabels)
plt.grid(ls="--",
         color="#000000",
         alpha=0.5,
         lw=1.5)
plt.contourf(data_mean,
             origin="lower",
             cmap="Greens")
plt.colorbar()
plt.show()
