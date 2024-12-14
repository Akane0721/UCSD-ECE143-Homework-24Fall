import pandas as pd


def add_month_yr(x):
    """
    Adds a new column 'month-yr' to the DataFrame x with the month and year extracted from the 'Timestamp' column.

    Args:
        x (pd.DataFrame): The input DataFrame containing a 'Timestamp' column.
    """
    assert isinstance(x, pd.DataFrame)
    MY = pd.to_datetime(x["Timestamp"]).dt.strftime("%b-%Y")
    id_index = x.columns.get_loc("ID")
    x.insert(id_index + 1, "month-yr", MY)
    return x


"""
data = pd.read_csv("survey_data.csv")
added = add_month_yr(data)
print(added)"""
