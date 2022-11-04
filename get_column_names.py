#Define function,Get coloumn names from a csv file
def get_column_names(data):
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """
    data = data.split('\n')
    k = []
    for i in data:
        a = i.split(',')
        k.append(a)
    return (k[0])

data = open('data.csv').read()

    
# Read the csv file