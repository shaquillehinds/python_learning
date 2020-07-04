# Create film list
films = {
    "Finding Dory": [3, 5],
    "Bourne": [18, 5],
    "Tarzan": [15, 5],
    "Ghost Busters": [12, 5]
}
cinema = True
while(cinema):
    # Ask user to pick a film
    print('='*25+'\n' * 2 +
          'Welcome to the cinema!''\n'
          'Please choose a film!''\n')
    for film in films.keys():
        print(film)
    # get user's choice
    chosen_film = input('--->').strip().title()
    # check if chosen film is in films
    if(not(chosen_film in films)):
        print('That film does not exist')
        continue
    # Ask user for their age
    age = int(input('How old are you?'))
    # if old enough and enough seats available let user book to see film
    if(age >= films[chosen_film][0] and films[chosen_film][1] > 0):
        print("Awesome you're booked to see the film!!")
        films[chosen_film][1] -= 1
        # else tell them they are not old enough or not enought seats availbable
    else:
        if(chosen_film == "Exit"):
            cinema = False
        elif(not(age >= films[chosen_film][0])):
            print("Sorry, you are not old enough to see this film.")
        else:
            print("Sorry, there are no more seats available")
