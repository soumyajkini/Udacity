def russian(a, b):
    x = a; y = b; z = 0
    
    while x > 0:
        if x % 2 == 1:
            z = z + y
        y = y << 1
        x = x >> 1
        print (x, y, z)
    return z

russian (63, 12)