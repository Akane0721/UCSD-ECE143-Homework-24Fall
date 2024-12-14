import csv


def write_columns(data, fname):
    """
    Writes three columns to a CSV file based on the input data

    Args:
        data (list): a list of int/float
        fname (str): name of the output file
    """
    assert isinstance(data, list) and isinstance(fname, str)
    assert all(isinstance(item, (int, float)) for item in data)

    with open(fname, "w", newline="") as file:
        writer = csv.writer(file)
        for d in data:
            ds = d**2
            dd = (d + ds) / 3
            writer.writerow([f"{d:.2f}", f"{ds:.2f}", f"{dd:.2f}"])
