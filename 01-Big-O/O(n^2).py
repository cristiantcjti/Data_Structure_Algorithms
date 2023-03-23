def print_items(n):
    '''
        The below is the equivalent Big O: n*n=n² = O(n²)
        It does not matter if it's O(n) to the 3rd, 4th, 10th, we always simply it as O(n²)
        It means it is a lot less efficient from a time complexity standpoint
    '''
    for i in range(n):
        for j in range(n):
            print(i,j) 

print_items(10)