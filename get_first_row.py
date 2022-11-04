def get_first_row(data):   
    """
    Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
    """
    data = data.split('\n')
    k = []
    for i in data:
        a = i.split(',')
        k.append(a)
    return (k[1])
data = open('data.csv').read()

   
   

# Read the csv file