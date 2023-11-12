from imports import sys
import tty
import termios

def lin_getpass(prompt="Password: "):
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        sys.stdout.write(prompt)
        sys.stdout.flush()
        password = ""
        while True:
            ch = sys.stdin.read(1)
            if ch in ['\n', '\r']:
                sys.stdout.write('\n')
                break
            elif ch == '\x7f':  # Backspace
                if len(password) > 0:
                    password = password[:-1]
                    sys.stdout.write('\b \b')
                    sys.stdout.flush()
            elif ch == '\x03':  # Handle Ctrl+C
                raise KeyboardInterrupt
            else:
                password += ch
                sys.stdout.write('*')
                sys.stdout.flush()
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return password