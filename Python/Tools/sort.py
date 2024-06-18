# featuring:
#   file content sorting
#   text input sorting
#   custom separators

def sort(user_input, separator=', ', isfile=False, sort_direction='asc'):
    separator = separator.replace("\\n", "\n") # handles newlines in input, so they don't get converted to \\n
    if isfile == True:
        file = open(user_input)
        sort_list = file.read()
        file.close()
        sort_list = sort_list.split(separator)
    else: sort_list = user_input.split(separator)
    
    print('unsorted:', sort_list)
    
    for _ in range(len(sort_list)-1):
        for i in range(len(sort_list)-1):
            # compares a to b and switches up their places if needed
            if sort_direction == 'asc':
                if sort_list[i] > sort_list[i+1]:
                    sort_list[i], sort_list[i+1] = sort_list[i+1], sort_list[i]
            
            if sort_direction == 'desc':
                if sort_list[i] < sort_list[i+1]:
                    sort_list[i], sort_list[i+1] = sort_list[i+1], sort_list[i]

    print('\nsorted:', sort_list)
    
    if isfile == True:
        file = open(user_input, "w")
        if '\n' in separator:
            file.write('\n'.join(sort_list))
        else: file.write(separator.join(sort_list))
        file.close()
    
    else: # for regular text input
        formatted_output = ''
        for i in range(len(list)-1): # add every item (except the last one) with a leading separator
            formatted_output += list[i]
            formatted_output += separator
        formatted_output += list[-1] # add the last item without leading separator
        print('\nformatted:', formatted_output)
    
    

 
if input('Sort file? (y/n): ') == 'y':
    sort(
        user_input=input('File path: '), 
        separator=input('Item separator: '), 
        isfile=True, 
        sort_direction=input('Sort direction (asc/desc): ')
    )
else:
    sort(
        user_input=input('Input text to sort:\n'), 
        separator=input('Item separator: '), 
        sort_direction=input('Sort direction (asc/desc): ')
    )