# Run the script for config

import subprocess
import sys
import argparse
import os


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


def timestamp_to_seconds(timestamp: str | float) -> float | None:
    # if already seconds, keep
    if isinstance(timestamp, (float, int)):
        return timestamp

    times = timestamp.split(':')
    # HH:mm:ss
    if len(times) == 3:
        h = times[0]*3600
        m = times[1]*60
        s = times[2]
        return float(h+m+s)
    
    # mm:ss
    elif len(times) == 2:
        m = times[1]*60
        s = times[2]
        return float(m+s)
    

# ===== ARGUMENTS =====
parser = argparse.ArgumentParser(
    formatter_class=argparse.RawTextHelpFormatter,
    add_help=False,
    description="Convert video to GIF using FFmpeg",
    epilog=f''' 
Example usage:
- default:\t\t%(prog)s -i video.mkv
- custom width:\t\t%(prog)s -i video.mkv -width 360
- part of a video:\t%(prog)s -i video.mkv -start 00:05:43 -duration 30
- part of a video:\t%(prog)s -i video.mkv -start 00:05:43 -end 00:07:14
- multiple videos:\t%(prog)s -i video.mkv video2.mp4 -fps 60''',
    usage='%(prog)s [OPTIONS] -i PATH [PATH...]'
)


general = parser.add_argument_group('General')
general.add_argument('-?', '-h', '-help', '--help', action='help', help='show help message')
inputs = parser.add_argument_group('Input')
inputs.add_argument('-input_filepath', '-i', nargs='+', metavar='PATH', help=r'Path to the input video file, e.g. C:\Memes\2000cheeses.mp4, or multiple paths separated by a whitespace.')
# inputs.add_argument('input_filepath', default='', metavar='PATH', help=r'Path to the input video file, e.g. C:\Memes\2000cheeses.mp4')
inputs.add_argument('-start', '-s', default=0, metavar='TIMESTAMP | SECONDS', help='Starting point in the video, e.g. 00:05:30, 05:30 or 330, 0.5 (default: 0)')
inputs.add_argument('-duration', '-end', '-t', metavar='TIMESTAMP | SECONDS', help='Timestamp to end at, or duration of the GIF in seconds, e.g. 01:26:10, 05:11 or 10, 0.5 (default: from the -start parameter to the end of the video)')

formatting = parser.add_argument_group('Format/Quality')
formatting.add_argument('-fps', default=15, metavar='FPS', help='GIF framerate, e.g. 15 (default 30)')
formatting.add_argument('-loop', '-l', default=0, metavar='COUNT', help='Loop (replay) count, e.g. 2 (to play 3x) (default: 0):\n\t0 => infinite,\n\t-1 => play once')
formatting.add_argument('-width', '-w', default=640, metavar='PX', help='GIF width in pixels, e.g. 720 (default: 640)\n\t-1 => original size')
formatting.add_argument('-dithering', '-d', type=int, default=0, metavar='0|1', help='Use dithering. Reduces filesize and improves performance, but makes GIF grainy (default: 0)')

debugging = parser.add_argument_group('Debugging')
debugging.add_argument('-pause', type=int, default=1, metavar='0|1', help='Keep the window open after finishing (for debugging) (default: 1)')


# ===== CODE =====    
if __name__ == '__main__':
    args = parser.parse_args()

    if not args.input_filepath:
        parser.print_help()
        input('\nPress Enter to exit...')
        exit()

    for file in args.input_filepath:
        output_filepath = file.rsplit('.', 1)[0] + '.gif'

        # if -duration not provided, go all in
        if not args.duration:
            args.duration = get_video_duration(file) - timestamp_to_seconds(args.start)
        # if -duration is a timestamp, use it as the point to end at, instead of a timer how long to run
        elif ":" in args.duration:
            # if -duration timestamp is less than start time
            if timestamp_to_seconds(args.duration) < timestamp_to_seconds(args.start):
                raise Exception('Duration/end timestamp is smaller than the starting time. Either lower -start, or increase -duration')
            else:
                args.duration = timestamp_to_seconds(args.duration) - timestamp_to_seconds(args.start)


        print(f'''Converting {file} to a GIF with:
- Framerate: {args.fps}
- Loop: {args.loop}
- Width: {args.width}
- Starting time: {args.start} seconds
- Duration: {args.duration} seconds
- Dithering: {bool(args.dithering)}''')

        # prepare FFmpeg command
        if args.dithering:
            ffmpeg_command = f'ffmpeg -ss {args.start} -t {args.duration} -i "{file}" -vf "fps={args.fps},scale={args.width}:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop {args.loop} "{output_filepath}"'
        else:
            ffmpeg_command = f'ffmpeg -ss {args.start} -t {args.duration} -i "{file}" -vf "fps={args.fps},scale={args.width}:-1:flags=lanczos,split[s0][s1];[s0]palettegen=stats_mode=diff[p];[s1][p]paletteuse=dither=none" -loop {args.loop} "{output_filepath}"'
        
        # Run
        try:
            subprocess.run(ffmpeg_command, shell=True, check=True)
            print(f'\nConversion complete: {output_filepath}')
        except subprocess.CalledProcessError:
            print('\nError: Conversion failed.')

    if args.pause:
        os.system("pause")
