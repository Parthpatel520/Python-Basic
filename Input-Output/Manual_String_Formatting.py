for x in range(1, 11):
    print(repr(x).ljust(2), repr(x*x).ljust(3), end = ' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).ljust(4))
    # print(repr(x*x*x*x).center(5))
    
print('12'.zfill(5))
print('3.14159265359'.zfill(5))

