def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    data = data.split('\n')
    k = []
    for i in data:
        a = i.split(',')
        k.append(a)
    return len(k[0])
data = open('data.csv').read()


# Read the csv file