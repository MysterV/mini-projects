import subprocess
import sys
import argparse
import os
import glob


# ===== ARGUMENTS SUPPORT =====
parser = argparse.ArgumentParser(
    formatter_class=argparse.RawTextHelpFormatter,
    add_help=False,
    description="Convert WAV <=> FLAC using FFmpeg",
    epilog=f'''Example usage:
- \t\t%(prog)s -i audio.wav
- \t\t%(prog)s -i audio.flac''',
    usage='%(prog)s [OPTIONS] -i PATH [PATH...]'
)

parser.add_argument('-?', '-h', '-help', '--help', action='help', help='show help message')
parser.add_argument('-input_filepath', '-i', nargs='+', metavar='PATH', help=r'Path to the input audio file, e.g. C:\Music\song.wav, or multiple paths separated by a whitespace.')
# parser.add_argument('input_filepath', default='', metavar='PATH', help=r'Path to the input video file, e.g. C:\Memes\2000cheeses.mp4')
parser.add_argument('-pause', action='store_true', help='Keep the window open after finishing (for debugging) (default: False)')
parser.add_argument('-overwrite', '-o', action='store_true', help='Overwrite existing files (default: False)')
parser.add_argument('-v', action='store_true', help='Show full logs (default: False)')


# ===== ENSURE 100% COMPATIBILITY =====

# Get sample format using ffprobe (e.g. pcm16, float32)
def get_sample_fmt(filepath):
    try:
        ffmpeg_command = f'ffprobe -v error -select_streams a:0 -show_entries stream=sample_fmt -of default=noprint_wrappers=1:nokey=1 "{filepath}"'
        if args.overwrite:
            ffmpeg_command = ffmpeg_command.replace('ffmpeg', 'ffmpeg -y')
        if not args.v:
            ffmpeg_command = ffmpeg_command.replace('ffmpeg', 'ffmpeg -hide_banner')
        
        result = subprocess.run(
            ffmpeg_command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=True
        )
        return result.stdout.strip()
    except Exception:
        print('Error: unable to automatically get original audio sample format. Exiting.')
        sys.exit(1)


# This is redundant, but whatever
FLAC_TO_WAV_CODEC = {
    "s16": "pcm_s16le",
    "s24": "pcm_s24le",
    "s32": "pcm_s32le",
    "fp16": "pcm_f16le",
    "fp24": "pcm_f24le",
    "fp32": "pcm_f32le"
}
# FLAC doesn't support float, so we have to convert to int
WAV_TO_FLAC_SAMPLE_FMT = {
    "s16": "s16",
    "s24": "s24",
    "s32": "s32",
    "fp16": "s24",
    "fp24": "s24",
    "fp32": "s24"
}



# ===== BRING IT ALL TOGETHER =====
def parse_paths(paths_arg):
    if not paths_arg:
        parser.print_help()
        input('\nPress Enter to exit...')
        exit()
    
    filepaths = []
    for path in paths_arg:
        expanded = glob.glob(path)
        if expanded:
            filepaths.extend(expanded)
        else:
            filepaths.append(path)
    return filepaths


if __name__ == "__main__":
    args = parser.parse_args()
    filepaths = parse_paths(args.input_filepath)
    
    
    for file in filepaths:
        filename, ext = file.rsplit('.', 1)
        if ext == 'wav': new_ext = '.flac'
        elif ext == 'flac': new_ext = '.wav'
        else:
            parser.print_help()
            input('\nPress Enter to exit...')
            exit()

        output_filepath = filename + new_ext
        sample_fmt = get_sample_fmt(file)
        print(f'====================\nConverting {file} to {new_ext}\n\n\n')


        # Build FFmpeg command
        if ext == 'wav':
            ffmpeg_command = f'ffmpeg -i "{filename}.wav" -map_metadata 0 -f ffmetadata - | ffmpeg -i "{filename}.wav" -c:a flac -map_metadata - "{filename}.flac"'
            # if sample_fmt in WAV_TO_FLAC_SAMPLE_FMT:
            #     ffmpeg_command = ffmpeg_command + f' -sample_fmt {WAV_TO_FLAC_SAMPLE_FMT[sample_fmt]}'
            if 'f' in sample_fmt:
                print('Its float, unsupported. SKIP.')
                continue
        elif ext == 'flac':
            ffmpeg_command = f'ffmpeg -i "{filename}.flac" -f ffmetadata - | ffmpeg -i "{filename}.flac" -c:a {FLAC_TO_WAV_CODEC[sample_fmt]} -map_metadata - "{filename}.wav"'
        if args.overwrite:
            ffmpeg_command = ffmpeg_command.replace('ffmpeg', 'ffmpeg -y')
        if not args.v:
            ffmpeg_command = ffmpeg_command.replace('ffmpeg', 'ffmpeg -hide_banner')

        try:
            print(f'Running {ffmpeg_command}')
            subprocess.run(ffmpeg_command, shell=True, check=True)
            print(f'\nConversion complete: {output_filepath}\n')
        except subprocess.CalledProcessError:
            print('\nError: Conversion failed.\n')

    print('\nFinished running.\n')
    if args.pause:
        os.system("pause")
