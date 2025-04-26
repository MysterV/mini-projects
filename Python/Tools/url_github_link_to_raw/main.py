import github_link_to_raw as gltr
import pyperclip

while True:
    link = input('GitHub file link (empty to exit):\n')
    if not link: break

    output = gltr.to_raw(link)
    if output:
        print(output)
        pyperclip.copy(output)
        print('Copied to clipboard!\n')
    else:
        print('Incorrect link format')
