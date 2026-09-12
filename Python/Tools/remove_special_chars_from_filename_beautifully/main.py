from pathlib import Path, WindowsPath
import re
import hashlib
import subprocess


# RULES
# write this in regex, reorder this list to adjust priority of conversions
regex_rules = [
    # separators
    (r'：\s', r' - '),
    (r'\s｜\s', r' - '),
    (r'⧸', r'-'),  # #TODO anything better?

    # question marks
    (r'(？)\s(\w+)', r' - \2'),  # abstract: unicode question mark followed by regular text (how? idk.mp4 -> how - idk.mp4)
    (r'(？)(\s*\S|$)', r'\2'),  # abstract: unicode question mark followed by special characters like a hyphen -, or end of file (how? - idk.mp4 -> how - idk.mp4 OR how?.mp4 -> how.mp4)

    (r'#(\d+)', r'\1'),  # abstract: hash followed by a number (#94 -> 94)

    # algorithm soup
    (r'\s#[a-zA-Z]+', r''),  # abstract: whitespace-hash-text that's not a number (title #music #tutorial -> title)
    (r'\s\[Piano\]', r''),
    (r'(\s*)「(.*)」', r'\1\2'),

    # quotes and frames
    (r'“', r''),
    (r'＂', r''),
    (r'【', r''),
    (r'】', r''),

    # emojis
    (r'\s*🖤', r''),
    (r'\s*🤣', r''),
]


def is_same_hash(path1, path2):
    hashes = []
    for path in (path1, path2):
        h = hashlib.sha256()
        with open(path, "rb") as file:
            while True:
                chunk = file.read(65535)
                if chunk == b'':
                    break
                else:
                    h.update(chunk)
        hashes.append(h.hexdigest())
    # print('\n'.join(hashes))
    return True if hashes[0] == hashes[1] else False


def rename_file(old_path: WindowsPath, new_path: WindowsPath):
    while True:
        try:
            old_path.rename(new_path)
            break
        except FileExistsError:
            if is_same_hash(old_path, new_path):
                old_path.unlink()
                break
            else:
                print('Conflict: 2 files with different contents would get renamed to the same name. Resolve this conflict by manually renaming one of them to something different.')
                print(old_path, '<-->', new_path)
                if input('Open explorer? y/n: ') == 'y':
                    print(old_path.absolute())
                    subprocess.run(['explorer.exe', rf'/select,{old_path.absolute()}'])
                    input('If the conflict is resolved, hit enter: ')
                else:
                    print('Conflict left unresolved.')
                    break


def rename_files_in_dir(folderpath: WindowsPath):
    paths = list(folderpath.iterdir())
    for path in paths:
        if path.is_file:
            new_stem = path.stem
            for r in regex_rules:
                new_stem = re.sub(r[0], r[1], new_stem)
            new_path = path.with_stem(new_stem)

            if path != new_path:
                rename_file(path, new_path)


# RENAME

if __name__ == '__main__':
    try:
        Path('test backup').copy('test')
    except FileExistsError:
        pass
    input('Press enter to run script')

    dir = Path('test')
    rename_files_in_dir(dir)
    print('Done!')
