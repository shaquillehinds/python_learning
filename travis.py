# Create a list of users
users = ['Dina', 'Deborah', 'Lloyen', 'Nalini']

run = True

while(run):
    # Get user's name
    name = input(
        "Salut! Je m'appelle Travis! \nComment t-appelles tu?").strip().title()

    if name == 'Exit':
        run = False
    # check if name is in the list users
    elif name in users:
        # get user's decision to be removed
        user_res = input(
            'Bienvenue {}. Do you want to be removed from the list (y/n)?'.format(name)).strip()
        # if decision is yes remove user
        if user_res.lower() == 'yes' or user_res.lower() == 'y':
            users.remove(name)
            print('Bye!')
            print(users)
        # else say bye
        else:
            print('Okay! Bye!')
    else:
        # get user's decision
        new_res = input(
            'Welcome {}. Do you want to be added to the users list (y/n)?'.format(name)).strip()
        if new_res.lower() == 'yes' or new_res.lower() == 'y':
            users.append(name)
            print('Welcome new user')
            print(users)
        else:
            print('Okay! Bye!')
