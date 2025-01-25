import pandas

nato_alphabet = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}

phrase = input('Phrase: ').upper()
phrase_code = [nato_alphabet_dict[letter] for letter in phrase.upper() if letter.isalpha()]
print(phrase_code)
