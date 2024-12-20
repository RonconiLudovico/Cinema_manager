# This is the main program so far, will be implemented in the future

from utils import loading
from utils.decision_making import *

def main():
    while True:
        choice = input("What would you like to do? ")
        navigate(choice)
        if choice == "9":
            break




if __name__ == "__main__":
    loading
    print(menus["0"])
    main()
