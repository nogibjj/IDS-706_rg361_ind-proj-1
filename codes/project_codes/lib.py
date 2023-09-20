"""This library file contains the common functions used in the project."""

def select_col(df, col_num=None):
    """This function takes in the polars DataFrame and user selected column number and returns the corresponding column if it is a valid numeric column,
    else it returns an error code. in case no input is provided, it returns the last column if it is numeric """
    
    #Check if user has selectd a column number, else assign it to last column. also assert valid column number is given
    if col_num == None:
        col = len(df.columns) - 1
    else:
        if (col_num > len(df.columns)) or(col_num <1) :
            return -1
        col = col_num - 1
    
    # get the column name
    col_name = df.columns[col]

    #check if this column has numeric data so that we can calculate the statistics and plot histogram
    if df[col_name].is_numeric():
        return col_name
    else:
        return -1
    
def summary_stats(df, col_name):
    return [df[col_name].mean(), df[col_name].median(), df[col_name].std()]
