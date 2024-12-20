from utils.assign_var import *

def screenings():
    header = "{:<30} {:<30} {:30}".format(Id , title, time)
    program = []

    for movie in movieList:
        rowMovie = "{:<30} {:<30} {:<30}".format(movie[Id], movie[title], movie[time])
        program.append(rowMovie)

    print(f"{header.upper()}\n\n{"\n\n".join(program)}\n")

def choose_movie():
    screenings()
    movieChoice = int(input("\nFor which projection would you like to book some seats? [Enter Id]\n"))
    print(select_seats(movieChoice))

def select_seats(movieId):
    seatsToBeBooked = input("\nHow many seats would you like to book? ")
    movieSchedule[movieId - 1][seats] -= int(seatsToBeBooked)
    return f"you have booked {seatsToBeBooked} seats for the movie {movieSchedule[movieId - 1][title]}\n"
