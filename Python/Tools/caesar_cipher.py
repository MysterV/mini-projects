def caesar(direction, message, shift='1'):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    message_processed = ''
    shift = int(shift)
    
    if direction not in ('encrypt', 'e', 'en', 'decrypt', 'd', 'de'):
        raise Exception('Invalid syntax! Expected "encrypt" or "decrypt" for direction.')
    if direction in ('decrypt', 'd', 'de'): shift *= -1

    for i in range(len(message)):
        if message[i] not in alphabet: message_processed += message[i]
        
        else:
            letter_index = (alphabet.index(message[i]) + shift) % 26
            if message[i].isupper(): letter_index += 26
            message_processed += alphabet[letter_index]

    return message_processed


def run():
    print(caesar(
        input('Do you wish to "encrypt" or "decrypt"?\n'),
        input('What is the message we\'re working with?\n'),
        input('What is the shift we\'re working with?\n')))

    if input('Run the cipher program again? y/n\n') == 'y':
        print('')
        run()

run()
