def change_separator(input, old, new):
    old = old.replace("\\n", "\n")
    new = new.replace("\\n", "\n")
    input_list = input.split(old)
    output = new.join(input_list)
    return output

print(change_separator(input('Text to format: '), input('Old separator: '), input('New separator: ')))