# simple file path to URL converter

from urllib.parse import quote

def URL_encode(path):
    path = list(path)
    if path[0] == '"': path.pop(0)
    if path[-1] == '"': path.pop(-1)
    
    for i in range(len(path)):
        if path[i] in (':', '/'): continue
        if path[i] == '\\': path[i] = '/'
        else:
            path[i] = quote(path[i])
    
    path = 'file://' + ''.join(path)
    return path

print(URL_encode(input('What path to encode?\n')))