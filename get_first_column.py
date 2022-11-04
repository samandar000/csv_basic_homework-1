def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    data = data.split('\n')
    k= []
    for i in data:
        a = i.split(',')
        k.append(a[0])
       
    return (k)
data = open('data.csv').read()



    
# Read the csv file