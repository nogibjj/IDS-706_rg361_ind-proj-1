""" Function to return the descriptive statistics of a Polars Dataframe"""
import polars as pl
import matplotlib.pyplot as plt
from lib import select_col


def descriptive_stats(fname, col=None):
    df = pl.read_csv(fname)

    col_name = select_col(df, col)

    #check if error code(-1) is received, if no error code-proceed further
    if col_name == -1:
        return "Please select valid column number"
    
    # create Histogram and save as output.png in output folder
    plt.hist(df.select(col_name))
    plt.ylabel("Count of " + col_name)
    plt.xlabel(col_name)
    plt.title("Data Loaded from : " + fname)
    plt.savefig("./resources/output.png")  # change the filepath here in case reequired
    plt.clf()

    # Write the summary statistics to a summary.md in output folder
    with open("./resources/summary.md", "w", encoding="utf-8") as f:
        f.write("Mean: " + str(df[col_name].mean()) + "\n")
        f.write("\n")
        f.write("Median: " + str(df[col_name].median()) + "\n")
        f.write("\n")
        f.write("Standard Deviation: " + str(df[col_name].std()))

    return [df[col_name].mean(), df[col_name].median(), df[col_name].std()]