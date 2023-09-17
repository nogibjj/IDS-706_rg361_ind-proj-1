"""Test file to verify main function"""

import polars as pl
from main import descriptive_stats


def test_stat():
    """Test main code agaisnt conditions"""

    fname = "./resources/blood_pressure.csv"
    # Create the polars DataFrame
    df = pl.read_csv(fname)

    # Test case 1: col number specified
    col = 3
    col_name = df.columns[col]
    assert [
        df[col_name].mean(),
        df[col_name].median(),
        df[col_name].std(),
    ] == descriptive_stats(fname, 4)

    # Test case 2: col number not specified, shoudl use last column
    col = 4
    col_name = df.columns[col]
    assert [
        df[col_name].mean(),
        df[col_name].median(),
        df[col_name].std(),
    ] == descriptive_stats(fname)


test_stat()
