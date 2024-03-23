def clear():
    import os
    # import subprocess
    if os.name in ('nt', 'dos'):
        os.system('cls')
        # subprocess.call('cls')
    elif os.name in ('linux', 'osx', 'posix'):
        os.system('clear')
        # subprocess.call('clear)
    else:
        print('\033c\033[H\033[3J', end='')