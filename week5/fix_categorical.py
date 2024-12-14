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


def fix_categorical(x):
    """
    Convert the month-yr column dtype to a Pandas CategoricalDtype with the correct order.

    Args:
        x (pd.DataFrame): The input DataFrame after adding a 'month-yr' column.
    """
    sorted_x = sorted(
        x["month-yr"].unique(), key=lambda x: pd.to_datetime(x, format="%b-%Y")
    )
    category = pd.CategoricalDtype(categories=sorted_x, ordered=True)
    x["month-yr"] = x["month-yr"].astype(category)
    # print(type(y))
    return x


data = pd.read_csv("survey_data.csv")
print(fix_categorical(add_month_yr(data)))
