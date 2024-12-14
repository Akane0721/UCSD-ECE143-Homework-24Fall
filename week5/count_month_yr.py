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


def count_month_yr(x):
    """
    Counting the amounts of different month-year pairs

    Args:
        x (pd.DataFrame): The input DataFrame after adding a 'month-yr' column.
    """
    assert isinstance(x, pd.DataFrame)
    my = x["month-yr"]
    counts = my.value_counts().sort_index().reset_index()
    counts.columns = ["month-yr", "Timestamp"]
    counts.set_index("month-yr", inplace=True)
    # print(counts)
    # print(type(counts))
    # print(counts["Timestamp"])
    return counts


data = pd.read_csv("survey_data.csv")
count_month_yr(add_month_yr(data))
