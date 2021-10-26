def calc_new_height():
    m = int(input("Enter the current width: "))
    n = int(input("Enter the current height: "))
    z = int(input("Enter the desired width: "))
    ratio = n/m
    new_height = z*ratio
    print("The corresponding height is:", new_height)
    return new_height
    
    
calc_new_height()
