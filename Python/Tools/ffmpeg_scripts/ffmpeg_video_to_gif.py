import subprocess
import sys
import argparse
import os

parser = argparse.ArgumentParser(
    description="Convert video to GIF using FFmpeg",
    epilog=f'''Example usage:
- default:\t\tffmpeg_video_to_gif.py video.mkv
- custom width:\t\tffmpeg_video_to_gif.py video.mkv -width 360
- part of a video:\tffmpeg_video_to_gif.py video.mkv -start 00:05:43 -duration 30''',
    formatter_class=argparse.RawTextHelpFormatter
)

# Get video duration using ffprobe
# Generally useless, could have instead made an if statement to call FFmpeg without the -t parameter, but this ensures 100% compatibility
def get_video_duration(filepath):
    try:
        result = subprocess.run(
            f'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "{filepath}"',
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=True
        )
        return float(result.stdout.strip())
    except Exception:
        print('Error: GIF duration not specified, and unable to automatically get original video duration. Exiting.')
        sys.exit(1)


parser.add_argument('-input_filepath', '-i', metavar='PATH', help=r'Path to the input video file, e.g. C:\Memes\2000cheeses.mp4')
parser.add_argument('-fps', default=15, metavar='INT', help='GIF framerate, e.g. 15 (default 30)')
parser.add_argument('-loop', '-l', default=0, metavar='INT', help='Loop (replay) count, e.g. 2 (to play 3x) (default: 0):\n\t0 => infinite,\n\t-1 => play once')
parser.add_argument('-width', '-w', default=640, metavar='pixels', help='GIF width, e.g. 720 (default: 640)\n\t-1 => original size')
parser.add_argument('-start', '-s', default=0, metavar='HH:mm:ss | mm:ss | SECONDS', help='Starting point in the video, e.g. 00:05:30, 05:30 or 330 (default: 0)')
parser.add_argument('-duration', '-t', metavar='HH:mm:ss | mm:ss | SECONDS', help='Duration of the GIF, e.g. 00:00:10, 00:10 or 10 (default: from -start to the end of the video)')
parser.add_argument('-pause', type=int, default=0, metavar='0|1', help='Keep the window open after finishing (for debugging) (default: 0)')
parser.add_argument('-dithering', '-d', type=int, default=0, metavar='0|1', help='Use dithering. Reduces filesize and improves performance, but makes GIF grainy (default: 0)')

args = parser.parse_args()

if not args.input_filepath:
    parser.print_help()
    input('\nPress Enter to exit...')
    exit()

output_filepath = args.input_filepath.rsplit('.', 1)[0] + '.gif'
if not args.duration:
    args.duration = get_video_duration(args.input_filepath) - float(args.start)


print(f'Converting {args.input_filepath} to a GIF with:')
print(f' - Framerate: {args.fps}')
print(f' - Loop: {args.loop}')
print(f' - Width: {args.width}')
print(f' - Starting time: {args.start} seconds')
print(f' - Duration: {args.duration} seconds')
print(f' - Dithering: {bool(args.dithering)}')



# FFmpeg command (single string)
if args.dithering:
    ffmpeg_command = f'ffmpeg -ss {args.start} -t {args.duration} -i "{args.input_filepath}" -vf "fps={args.fps},scale={args.width}:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop {args.loop} "{output_filepath}"'
else:
    ffmpeg_command = f'ffmpeg -ss {args.start} -t {args.duration} -i "{args.input_filepath}" -vf "fps={args.fps},scale={args.width}:-1:flags=lanczos,split[s0][s1];[s0]palettegen=stats_mode=diff[p];[s1][p]paletteuse=dither=none" -loop {args.loop} "{output_filepath}"'

try:
    subprocess.run(ffmpeg_command, shell=True, check=True)
    print(f'\nConversion complete: {output_filepath}')
except subprocess.CalledProcessError:
    print('\nError: Conversion failed.')

if args.pause:
    os.system("pause")
