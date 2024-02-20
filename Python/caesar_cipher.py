def caesar(direction, message, shift='1'):
    if direction != 'encrypt' and direction != 'decrypt': raise Exception('Invalid syntax! Expected "encrypt" or "decrypt" for direction.')
    if not shift.isnumeric(): raise Exception('Invalid syntax! Expected an integer.')

    shift = int(shift)
    if direction == 'decrypt': shift *= -1
    from assets import alphabet # contains both lowercase and uppercase letters
    message_processed = ''

    for _ in range(len(message)):
        if message[_] not in alphabet: # account for non-letter characters
            message_processed += message[_]

        else:
            letter_index = (alphabet.index(message[_])+shift)%26
            if message[_].isupper(): letter_index += 26 # account for uppercase letters
            
            message_processed += alphabet[letter_index]


    print(message_processed)

def run():
    try:
        caesar(
            input('Do you wish to "encrypt" or "decrypt"?\n'),
            input('What is the message we\'re working with?\n'),
            input('What is the shift we\'re working with?\n'))
    except:
        print('Wrong syntax!')
        run()
    if input('Do you want to run the cipher program again? y/n\n') == 'y': run()

run()
