import re

def get_note_midi_number(key: str) -> int:
    '''returns the MIDI number of the note'''
    key_analyzed = re.match('(^[a-g])([b#]*)(-*\d+)', key.lower())
    if not key_analyzed: raise Exception('Incorrect note format')

    note, accidental, octave = key_analyzed.groups()
    octave = int(octave)
    notes = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']
    note_number = (notes.index(note) + (octave+1)*12)
    
    if accidental:
        for b in range(accidental.count('b')): note_number -= 1  # down a semitone
        for sharp in range(accidental.count('#')): note_number += 1  # up a semitone
    return note_number

def piano_key_frequency(key: int|str='A4', tuning: float=440.0, tuning_ref_key: int|str='A4', round_digits: int=3) -> dict:
    '''
    Takes in the key in the form of either:
    \n- {1 letter note name}{however many accidentals you want}{octave number}, e.g. A#4, D##b#b11,
    \n- the MIDI number of the note, e.g. 70,
    \nReturns the frequency of that note.
    \nSupports multi-accidentals and notes outside of the a piano's scale
    '''
    # if the input is the key name, e.g. A#4, get the MIDI number of the keys first
    if isinstance(key, str):
        note_number = get_note_midi_number(key)
    elif isinstance(key, int): note_number = key

    if isinstance(tuning_ref_key, str):
        ref_note_number = get_note_midi_number(tuning_ref_key)
    elif isinstance(tuning_ref_key, int): ref_note_number = tuning_ref_key
    
    return round((tuning * 2 ** ((note_number-ref_note_number)/12)), round_digits)

