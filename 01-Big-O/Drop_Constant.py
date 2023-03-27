def print_items(n):
    '''
        The below is the equivalent Big O: O(2n) 
        Applying Drop constant:
        Just remove the number constant 2: O(n)
    '''
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)


print_items(10)