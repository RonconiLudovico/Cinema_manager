import time

def loading():

    for i in range(7):
        print('\rloading' + '.' * i,  end=".")
        time.sleep(0.5)

    time.sleep(0.5)
    print(r"""
                             ____________________________
                            |                            |
                            |        CINEMA SCREEN       |
                            |____________________________|

                         .-'                              '-.
                        /                                    \
                       /                                      \
                      /________________________________________\
                     /                                          \
                    /                                            \


    Welcome to Cinema Manager!
    Manage Reservations, Check screenings and more with ease!
    """)

loading()
