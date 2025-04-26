import piano_key_frequency as pkf
import pandas

notes = ['c0', 'a4', 'a#4', 'b4', 'c5', 'c#5', 'd5', 'd#5', 'e5', 'f5', 'f#5', 'g5', 'g#5', 'A5', 'a##5', 'dbbbbb5', 'Ab#b#b#b#b#5', 'A-1', 'C-10', 'C12', 'D20', 69, 1024]
speed = 344  # speed of sound

output = []
for i in notes:
    frequency = pkf.piano_key_frequency(i)
    wavelength = speed/frequency *100
    output.append({
        'note': i,
        'frequency (Hz)': frequency,
        'length (cm)': wavelength,
        'speed (m/s)': speed
    })
    # print(f'{i}\t\tfrequency [Hz]: {frequency:.2f}\tlength [cm]: {wavelength:.6f}\tspeed [m/s]: {speed}')
output_formatted = pandas.DataFrame(output, index=notes)
print(output_formatted.to_string(index=False, float_format=lambda x: f"{x:.3e}" if abs(x) >= 1e7 else f"{x:.3f}"))

# TODO:
# add volume parameter
# calculate how the note volume is perceived by the human
# calculate the energy / power of the note
# calculate the attenuation for that note
# calculate how far will the note go before becoming inaudible
