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
    
    k = data[0].split(',')
    return (k)

data = open('data.csv').read()


    
# Read the csv file