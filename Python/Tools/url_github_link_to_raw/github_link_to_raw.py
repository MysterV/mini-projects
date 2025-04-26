# A simple GitHub file link to raw file contents link converter

import re

def to_raw(link: str) -> str:
    match = re.match('https://github.com/(.+/)(.+/)blob/(.+/)(.*)', link)
    if match: user, repo, branch, path = match.groups()
    else: return
    return f'https://raw.githubusercontent.com/{user}{repo}{branch}{path}'

