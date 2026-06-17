# script to be called from the terminal, check the help function for details
# requires ffmpeg and ffprobe to be added to PATH
# tends to break if the file has chapters

import subprocess
import argparse
import os
import glob


# ===== ARGUMENTS =====
parser = argparse.ArgumentParser(
    formatter_class=argparse.RawTextHelpFormatter,
    add_help=False,
    description="A solution to cut off the annoying intros and outros from downloaded music using FFmpeg",
    epilog=''' 
Example usage:

Trimming:
- beginning (seconds):\t\t\tpython %(prog)s -i audio.wav -start 10.5
- beginning (timestamp):\t\tpython %(prog)s -i audio.wav -s 0:10.5
- end (seconds):\t\t\tpython %(prog)s -i audio.wav -end 70
- end (timestamp):\t\t\tpython %(prog)s -i audio.wav -to 1:10
- beginning and end (timestamp):\tpython %(prog)s -i audio.wav -s 1:10 -end 2:05.5

Multiple files at once:
- list one by one:\t\t\tpython %(prog)s -i audio.wav audio2.wav -s 3
- or use entire folders:\t\tpython %(prog)s -i C:\\music -s 3
- or use wildcards:\t\t\tpython %(prog)s -i *.wav -s 3
- works for folders:\t\t\tpython %(prog)s -i C:\\music\\* -s 3''',
    usage='%(prog)s [OPTIONS] -i PATH [PATH...]',
    allow_abbrev=False
)


general = parser.add_argument_group('General')
general.add_argument('-?', '-h', '-help', '--help', action='help', help='show help message')

inputs = parser.add_argument_group('Input')
inputs.add_argument('-input_filepath', '-i', nargs='+', metavar='PATH', help=r'Path to the input audio file, e.g. C:\Music\song.wav, or multiple paths separated by a whitespace.')
inputs.add_argument('-start', '-s', default=0, metavar='TIMESTAMP | SECONDS', help='Starting point in the video, e.g. 00:05:30, 05:30 or 330, 0.5 (optional, default: 0)')
inputs.add_argument('-end', '-to', metavar='TIMESTAMP | SECONDS', help='Timestamp to end at, or duration in seconds, e.g. 01:26:10, 05:11 or 10, 0.5 (optional, default: from the -start parameter to the end of the video)')

outputs = parser.add_argument_group('Output')
outputs.add_argument('-overwrite', '-o', action='store_true', help='Overwrite existing files (default: False)')

debugging = parser.add_argument_group('Debugging')
debugging.add_argument('-v', action='store_true', help='Show full logs (default: False)')
debugging.add_argument('-nopause', action='store_true', help='Add to not pause the window after finishing')



# ===== PROCESSING =====
def parse_paths(paths_arg):
    if not paths_arg:
        print('No path provided.')
        parser.print_help()
        input('\nPress Enter to exit...')
        exit()
    
    filepaths = []
    for path in paths_arg:
        if os.path.isdir(path):
            filepaths.extend(
                os.path.join(path, f)
                for f in os.listdir(path)
                if os.path.isfile(os.path.join(path, f))
            )
        else:
            expanded = glob.glob(path)
            if expanded:
                filepaths.extend(f for f in expanded if os.path.isfile(f))
            else:
                filepaths.append(path)
    return filepaths


def process_file(file):
    # process the path
    filename, ext = file.rsplit('.', 1)
    output_filepath = filename + "-trim." + ext

    print(f'====================\nTrimming {file} from {args.start if args.start else 'the start'} to {args.end if args.end else 'the end'}\n\n\n')


    # Build FFmpeg command
    start = f' -ss {args.start}' if args.start else ''
    end = f' -to {args.end}' if args.end else ''

    ffmpeg_command = f'ffmpeg -i "{filename}.{ext}"{start}{end} -map 0 -c copy -map_metadata 0 "{output_filepath}" '


    if args.overwrite:
        ffmpeg_command = ffmpeg_command.replace('ffmpeg', 'ffmpeg -y')
    if not args.v:
        ffmpeg_command = ffmpeg_command.replace('ffmpeg', 'ffmpeg -hide_banner')

    try:
        print(f'Running {ffmpeg_command}')
        subprocess.run(ffmpeg_command, shell=True, check=True)
        print(f'\nTrimming complete: {output_filepath}\n')
    except subprocess.CalledProcessError:
        print('\nError: Trimming failed.\n')


# ===== RUN =====
if __name__ == "__main__":
    print(__file__)
    args = parser.parse_args()
    print(args)
    filepaths = parse_paths(args.input_filepath)
    
    for file in filepaths:
        process_file(file)
        
    print('\nFinished running.\n')
    if not args.nopause:
        os.system("pause")
