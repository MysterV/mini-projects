import re

def piano_key_wave(key: str, tuning: float=440.0, tuning_key: str='A4') -> dict:
    '''
    Takes a key in the form \<note name>\<accidental>\<octave>, e.g. A#4,
    and returns the frequency of that note.
    \nSupports multi-accidentals and notes outside of the a piano's scale
    '''
    key_analyzed = re.match('(^[a-g]{1})([b#]*)(-*\d+)', key.lower())
    note, accidental, octave = key_analyzed.groups()
    octave = int(octave)
    notes = ['a', 'a#', 'b', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#']

    note_number = notes.index(note)  # scale degree, 1-7
    if accidental:
        for b in range(accidental.count('b')):
            note_number -= 1  # down a semitone
        for sharp in range(accidental.count('#')):
            note_number += 1  # up a semitone

    return tuning * 2 ** (octave-4 + (note_number)/12)
    # moves you down to A0, and then moves you up to the right octave, then shifts to the right degree

notes = ['a4', 'a#4', 'b4', 'c5', 'c#5', 'd5', 'd#5', 'e5', 'f5', 'f#5', 'g5', 'g#5']
for i in notes:
    print(piano_key_wave(i))

