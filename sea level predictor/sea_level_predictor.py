import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv("epa-sea-level.csv")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], alpha=0.6, label="Data")

    slope, intercept, r_value, p_value, std_err = linregress(
        df["Year"], df["CSIRO Adjusted Sea Level"]
    )
    years_extended = pd.Series(range(1880, 2051))
    ax.plot(
        years_extended,
        intercept + slope * years_extended,
        "r",
        label="Best Fit (1880–2050)",
    )

    df_recent = df[df["Year"] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(
        df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"]
    )
    years_recent = pd.Series(range(2000, 2051))
    ax.plot(
        years_recent,
        intercept2 + slope2 * years_recent,
        "g",
        label="Best Fit (2000–2050)",
    )

    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    ax.legend()

    fig.tight_layout()
    fig.savefig("sea_level_plot.png")
    return fig
