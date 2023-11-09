from imports import getpass, login, get_grades, print_grades, get_creds
uid, token = str, str
for i in range(3):
    username, password = get_creds()
    uid, token, error = login(username, password)
    if error:
        print(f'\n{error}\n')
        if i < 2:
            pass
        else:
            getpass('Too many errors, please retry in a few moments, exiting...')
            exit(1)
    elif uid and token:
        break
grades, average = get_grades(uid, token)
print_grades(grades, average)
getpass('Press enter to exit...')