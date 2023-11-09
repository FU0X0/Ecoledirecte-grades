from imports import getpass, urlparsequote
from platform import system
def get_creds():
    try:

        username = input("Nom d'utilisateur : ")
        password = ""
        if system() == "Windows":
            from winpass import win_getpass
            password = win_getpass("Mot de passe : ")
        elif system() in ["Linux", "Darwin"]:
            from linpass import lin_getpass
            password = lin_getpass("Mot de passe : ")
        else:
            getpass("Platform not supported, exiting...")
            exit(1)
    except KeyboardInterrupt:
        print('\nExiting...')
        exit(0)
    return username, urlparsequote(password)