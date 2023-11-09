import msvcrt

def win_getpass(prompt="Password: "):
    print(prompt, end='', flush=True)
    password = ""
    while True:
        ch = msvcrt.getwch()  # Use getwch() to get wide characters (Unicode)
        if ch in ['\r', '\n']:
            print()
            break
        elif ch == '\x08':  # Backspace
            if len(password) > 0:
                password = password[:-1]
                print('\b \b', end='', flush=True)  # Erase the last asterisk
        elif ch == '\x03':  # Handle Ctrl+C
            raise KeyboardInterrupt
        else:
            password += ch
            print('*', end='', flush=True)  # Print an asterisk for each character typed
    return password