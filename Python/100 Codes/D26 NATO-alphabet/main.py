import pandas
import os
import inflect
import unicodedata

nato_alphabet = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}

phrase = input('Phrase: ').upper()
phrase_code = []
for letter in phrase.upper():
    if letter.isalpha():
        phrase_code.append(nato_alphabet_dict[letter])
    elif letter.isnumeric():
        phrase_code.append(inflect.engine().number_to_words(letter).title())
    else:
        phrase_code.append(unicodedata.name(letter).title())

with open('output.txt', 'wt') as f:
    f.write(' '.join(phrase_code))
os.startfile('output.txt')
