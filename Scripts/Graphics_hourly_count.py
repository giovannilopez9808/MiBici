import matplotlib.pyplot as plt
from Functions import *


def format_data(data: DataFrame) -> DataFrame:
    data.index = pd.to_datetime(data.index)
    return data


parameters = {"path data": "../Output/",
              "file data": "Hourly_count.csv"}

data = read_data(parameters["path data"],
                 parameters["file data"],
                 use_index=True)
data = format_data(data)
data = data.mean()
plt.subplots(figsize=(8, 4))
plt.plot(data.index, data,
         marker="o")
plt.show()
