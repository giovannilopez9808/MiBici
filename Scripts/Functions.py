import pandas as pd


def format_data(data: pd.DataFrame):
    data.index = pd.to_datetime(data["Date"])
    data = data.drop(columns="Date")
    return data


def read_data(path: str, file: str):
    data = pd.read_csv("{}{}".format(path, file))
    return data
