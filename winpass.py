import msvcrt

def win_getpass(prompt="Password: "):
    print(prompt, end='', flush=True)
    password = ""
    alt_gr, t = False, False
    while True:
        if alt_gr:
            if t:
                alt_gr, t = False, False
            else:
                t = True
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
        elif ch == '\x00':
            alt_gr = True
        elif ch in ['\x79', '\x7e'] and alt_gr:
            pass
        else:
            password += ch
            print('*', end='', flush=True)  # Print an asterisk for each character typed
    return password