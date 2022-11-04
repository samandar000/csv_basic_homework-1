def get_first_row(data):   
    """
    Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
    """
    data = data.split('\n')
    
    k = data[1].split(',')
    
    return (k)
data = open('data.csv').read()

   

# Read the csv file