def get_days(s, m, h):
    m = m+(s/60)
    h = h+(m/60)
    days = round(h/24, 4)
    return days

def convert_to_days():
    hours = int(input("Enter number of hours: "))
    minutes = int(input("Enter number of minutes: "))
    seconds = int(input("Enter number of seconds: "))
    days = get_days(seconds, hours, minutes)
    print("The number of days is:", days)
    
convert_to_days()
