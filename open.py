def main():
    #try:
      #  open("/path/to/mars.jpg")
    #except FileNotFoundError:
     #   print("Couldn't find the config.txt file!")
    try:
        open("config.txt")
    except OSError as err:
         if err.errno == 2:
             print("Couldn't find the config.txt file!")
         elif err.errno == 13:
             print("Found config.txt but couldn't read it")

def water_left(astronauts, water_left, days_left):
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    return f"Total water left after {days_left} days is: {total_water_left} liters"

if __name__ == '__main__':
    main()
    water_left(5, 100, 2)