# simple Windows file path to URL converter

from urllib.parse import quote
import re


def to_uri(path: str, protocol: str='file://', address: str='/'):
    # path_list = list(path)
    # remove quotes, e.g. "B:\folder\file name" => B:\folder\file name
    # and separate drive letter (if exists)
    drive_letter = ''
    split_path = re.match(r'\"([A-Za-z]:)\\(.*)\"', path)
    if split_path:
        drive_letter, path = split_path.groups()
    path_list = list(path)

    # convert characters, e.g. B:\folder\file name => B:/folder/file%20name
    for i in range(len(path_list)):
        if path_list[i] == ':': continue  # prevent % formatting
        elif path_list[i] == '\\': path_list[i] = '/'  # \ => /
        else:
            path_list[i] = quote(path_list[i])
    path = ''.join(path_list)
    

    # optionally trim drive letters, e.g. B:/folder/file%20name => /folder/file%20name
    if protocol == 'http://' or protocol == 'https://':
        return protocol + address + path
    elif drive_letter:
        return protocol + address + drive_letter + '/' + path
    else:
        return protocol + address + path
