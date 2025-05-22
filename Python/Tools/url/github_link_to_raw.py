# A simple GitHub file link to raw file contents link converter

import re

def to_raw(link: str) -> str:
    match = re.match('https://github.com/(.+/)(.+/)blob/(.+/)(.*)', link)
    if match: user, repo, branch, path = match.groups()
    else: return
    return f'https://raw.githubusercontent.com/{user}{repo}{branch}{path}'


if __name__ == '__main__':
    import pyperclip
    while True:
        link = input('GitHub file link (empty to exit):\n')
        if not link: break

        output = to_raw(link)
        if output:
            print(output)
            pyperclip.copy(output)
            print('Copied to clipboard!\n')
        else:
            print('Incorrect link format')