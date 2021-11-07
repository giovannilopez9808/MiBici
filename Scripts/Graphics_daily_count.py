import matplotlib.pyplot as plt
import pandas as pd


def format_data(data: pd.DataFrame):
    data.index = pd.to_datetime(data["Date"])
    data = data.drop(columns="Date")
    return data


parameters = {"path data": "../Output/",
              "file data": "Daily_count.csv"}
data = pd.read_csv("{}{}".format(parameters["path data"],
                                 parameters["file data"]))
data.columns = ["Date", "Count"]
data = format_data(data)
data = data.resample("MS").mean()
plt.subplots(figsize=(9, 3))
plt.scatter(data.index, data["Count"])
plt.tight_layout()
plt.show()
