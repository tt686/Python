print("  x  1  2   3   4   5   6   7   8   9   10   11   12   13")
for x in range(1,13): 
    mult_table = ' '
    for y in range(0, 13):
        if y is 0:
            mult_table += ' ' + str(x)
        else:    
            mult_table += '  ' + str(y * x)
    print mult_table
