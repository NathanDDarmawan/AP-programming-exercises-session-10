def convert_to_celsius(f):
    celsius = (5/9)*(f-32)
    return celsius
    
def convert_to_kelvin(f):
    kelvin = f+273.15
    return kelvin
    
def convert_temp():
    F = int(input("Enter a temperature in Fahrenheit: "))
    C = convert_to_celsius(F)
    K = convert_to_kelvin(C)
    
    print("The temperature in Fahrenheit is:", F)
    print("The temperature in Celsius is:", C)
    print("The temperature in Kelvin is:", K)
    
convert_temp()
