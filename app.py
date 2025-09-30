import hvplot.pandas  # noqa: F401, F811
import numpy as np  # noqa: F811
import pandas as pd
import panel as pn

PRIMARY_COLOR = "#0072B5"
SECONDARY_COLOR = "#B54300"
CSV_FILE = (
    "https://raw.githubusercontent.com/holoviz/panel/main/examples/assets/occupancy.csv"
)


@pn.cache
def get_data():
    return pd.read_csv(CSV_FILE, parse_dates=["date"], index_col="date")


data = get_data()


def transform_data(variable, window, sigma):
    """Calculates the rolling average and identifies outliers"""
    avg = data[variable].rolling(window=window).mean()
    residual = data[variable] - avg
    std = residual.rolling(window=window).std()
    outliers = np.abs(residual) > std * sigma
    return avg, avg[outliers]


def get_plot(variable="Temperature", window=30, sigma=10):
    """Plots the rolling average and the outliers"""
    avg, highlight = transform_data(variable, window, sigma)
    return avg.hvplot(
        height=300, legend=False, color=PRIMARY_COLOR
    ) * highlight.hvplot.scatter(color=SECONDARY_COLOR, padding=0.1, legend=False)


variable = pn.widgets.Select(
    name="variable", value="Temperature", options=list(data.columns)
)
window = pn.widgets.IntSlider(name="window", value=30, start=1, end=60)
sigma = pn.widgets.IntSlider(name="sigma", value=10, start=0, end=20)
plot = pn.bind(get_plot, variable=variable, window=window, sigma=sigma)
pn.GridBox(variable, window, sigma, plot).servable()
