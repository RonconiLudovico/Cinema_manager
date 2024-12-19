import time

def loading():

    for i in range(7):
        print('\rloading' + '.' * i,  end=".")
        time.sleep(0.5)

    time.sleep(0.5)
    print(f"\n\nWelcome to the Cinema manager! How can I help you today?\n")

loading()
