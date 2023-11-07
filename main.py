from __init__ import urlparsequote, getpass, login, get_grades, print_grades
uid, token = str, str
for i in range(3):
    username = input("Nom d'utilisateur : ")
    password = urlparsequote(getpass("Mot de passe : "))
    try:
        uid, token = login(username, password)
        break
    except IndexError:
        print('\nInvalid username or password\n')
        if i < 2:
            pass
        else:
            print('Too many errors, please retry in a few moments, exiting...')
            exit(1)
notes, moyenne = get_grades(uid, token)
print_grades(notes, moyenne)
getpass('Press enter to exit...')