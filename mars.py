try:
    open("mars.jpg")
except FileNotFoundError as err:
        print("got a problem trying to read the file:", err)