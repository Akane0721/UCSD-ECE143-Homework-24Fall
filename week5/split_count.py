import pandas as pd


def split_count(x):
    """
    Take csv column as input and output Pandas dataframe counting the splitted values

    Args:
        x (pd.Series): The input series with string values
    """
    assert isinstance(x, pd.Series)
    all = x.str.split(",").sum()
    counts = pd.Series(all).str.strip().value_counts()
    sorted_counts = counts.sort_values(ascending=True).reset_index()
    sorted_counts.columns = ["", "Count"]
    sorted_counts.set_index("", inplace=True)
    sorted_counts.index.name = None
    print(type(sorted_counts), "\n")
    return sorted_counts


data = pd.read_csv("survey_data.csv")
counts = split_count(
    data["Is there anything in particular you want to use Python for?"]
)
print(counts)
