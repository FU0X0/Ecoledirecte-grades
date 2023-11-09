from imports import getpass, login, get_grades, print_grades, get_creds
uid, token = str, str
for i in range(3):
    try:
        username, password = get_creds()
        uid, token = login(username, password)
        break
    except IndexError:
        print('\nInvalid username or password\n')
        if i < 2:
            pass
        else:
            getpass('Too many errors, please retry in a few moments, exiting...')
            exit(1)
notes, moyenne = get_grades(uid, token)
print_grades(notes, moyenne)
getpass('Press enter to exit...')