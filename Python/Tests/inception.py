# Question 1
print('Is it possible to put a dictionary inside a list?')
try:
    list1 = []
    dict1 = {}

    list1.append(dict1)
    print(list1)
except: print('Guess not. It threw an error.')


# Question 2
print('\n\nIs it possible to put a list inside a dictionary...')
list2 = []
dict2 = {}

try:
    print('as a key?')
    dict2[list1] = 'value'
    print(dict2)
except: print('Guess not. It threw an error.') # that a list is not hashable

try:
    print('\nas a value?')
    dict2['key'] = list2
    print(dict2)
except: print('Guess not. It threw an error.')


# Question 3
print('\n\nIs it possible to put a list inside a list inside a list inside a list inside a list... etc.?')
try:
    list3 = []
    for _ in range(10):
        list4 = []
        list4.append(list3)
        list3 = list4
    print(list3)

except: print('Guess not. It threw an error.')

# Question 4
print('\nIs it possible to access a list inside a list... etc.?')
def access_innermost_list(nested_list, text):
    for _ in nested_list:
        if isinstance(_, list):
            access_innermost_list(_, text)
    
    if len(nested_list) == 0:
        nested_list.append(text)

try:
    access_innermost_list(list3, 'Yup.')
    print(list3)

except: print('Guess not. It threw an error.')


# Question 5
print('\n\nIs it possible to put a dictionary inside a dictionary...')
dict3 = {}

try:
    print('as a key?')
    dict4 = {}
    dict3[dict4] = 'value'
    print(dict3)
except: print('Guess not. It threw an error.') # that a dictionary is not hashable

try:
    print('\nas a value?')
    dict4 = {}
    dict3['key'] = dict4
    print(dict3)
except: print('Guess not. It threw an error.')


# Question 6
print('\n\nIs it possible to put a dictionary inside a dictionary inside a dictionary... etc.?')
try:
    dict3 = {}
    for _ in range(10, 0, -1):
        dict4 = {}
        dict4[_] = dict3
        dict3 = dict4
    print(dict3)

except: print('Guess not. It threw an error.')


# Question 7
print('\n\nIs it possible to access a dictionary inside a dictionary inside a dictionary... etc.?')
def access_innermost_dict(nested_dict, key, value):
    for _ in nested_dict:
        if isinstance(nested_dict[_], dict):
            access_innermost_dict(nested_dict[_], key, value)
    if len(nested_dict) == 0:
        nested_dict[key] = value

try:
    access_innermost_dict(dict3, 'answer', 'Yup.')
    print(dict3)
    
except: print('Guess not. It threw an error.')

# Question 8
print('\n\n\nDo the same rules apply to tuples as well?')
try:
    print('Is it possible to put a dictionary, a list and a tuple inside of a tuple?')
    tuple1 = ({'answer': 'Yup.'}, ['Of course!'], ('Why not?'))
    print(tuple1)
except: print('Guess not. It threw an error.')

try:
    print('\nIs it possible to put a tuple inside a tuple inside a tuple inside a tuple... etc.?')
    tuple1 = ()
    for _ in range(10):
        tuple2 = (tuple1,)
        tuple1 = tuple2
    print('Kinda...\n', tuple1)
except: print('Guess not. It threw an error.')

print('\nBut obviously you can\'t modify a tuple... right?')
def access_innermost_tuple(nested_tuple, text):
    for _ in nested_tuple:
        if isinstance(_, tuple):
            access_innermost_tuple(_, text)
    if len(nested_tuple) == 0:
        nested_tuple = ('Yup.',)

try:
    access_innermost_tuple(tuple1, 'Yup.')
    print(tuple1)
    print('Unfortunately not. Tuples cannot be modified, but you can always generate a new one.')
    tuple3 = ('shiny new tuple')
    for _ in range(10):
        tuple4 = (tuple3,)
        tuple3 = tuple4
    print(tuple3)

except: print('Guess not. It threw an error.')