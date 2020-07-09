from os import system, name


def clear_screen():
    if name == 'nt':      # for windows
        _ = system('cls')
    else:                 # for mac and linux(here, os.name is 'posix')
        _ = system('clear')
