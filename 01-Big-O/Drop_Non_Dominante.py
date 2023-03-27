def print_items(n):
    '''
        The below is the equivalent Big O:
            first two loops:  O(n²)
            last loop: O(n)
            results: O(n²) + O(n) = O(n² + n)

        When we start having large numbers (n), in squared (n²) is going to significantly increse while 
        the second (n) becomes insignificant in comparison.
        In this equation, (n²) is the dominant term and that stand alone (n) is the non-dominant term.
        Thus, we just drop the non-dominants O(n² + n) = O(n²)
    '''
    for i in range(n):
        for j in range(n):
            print(i,j)
    
    for k in range(n):
        print(k)

print_items(10)