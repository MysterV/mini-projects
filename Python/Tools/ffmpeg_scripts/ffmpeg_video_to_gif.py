
import subprocess
import sys

# Get video duration using ffprobe
def get_video_duration(input_file):
    try:
        result = subprocess.run(
            f'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "{input_file}"',
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=True
        )
        return float(result.stdout.strip())
    except Exception:
        print('Error: GIF length not specified, unable to get original video duration from input file. Exiting.')
        sys.exit(1)

# Argument Parsing
if len(sys.argv) < 2:
    print('Usage: ffmpeg_video_to_gif.py <path> [fps] [loop] [width] [start] [duration]')
    print('\nParameters: (to use a specific parameter (e.g. width), you need to provide every parameter before it (e.g. fps loop width))')
    print('fps (default 30): specify GIF framerate')
    print('loop: 0 -> infinite, -1 -> no, 1+ -> specify loop count (default 0)')
    print('width: -1 -> original size, 1+ -> specify GIF width (default 640)')
    print('start: specify timestamp or time in seconds in the video to start at (default 0)')
    print('duration: duration of the GIF in seconds (default - calculated as (video length-start))')
    print(f'\nExample: navigate to the folder where the video you want to convert is and run:')
    print(f'Example1 (default parameters): {__file__} video.mkv')
    print(f'Example2 (custom): {__file__} video.mkv 60 0 -1 00:05:43 30')
    input('\nPress Enter to exit...')
    sys.exit(1)

input_file = sys.argv[1]
output_file = input_file.rsplit('.', 1)[0] + '.gif'

fps = sys.argv[2] if len(sys.argv) > 2 else 30
loop = sys.argv[3] if len(sys.argv) > 3 else 0
width = sys.argv[4] if len(sys.argv) > 4 else 640
start_time = sys.argv[5] if len(sys.argv) > 5 else 0
duration = sys.argv[6] if len(sys.argv) > 6 else (get_video_duration(input_file) - float(start_time))


# FFmpeg command (single string)
ffmpeg_command = (
    f'ffmpeg -ss {start_time} -t {duration} -i "{input_file}" -vf "fps={fps},scale={width}:-1:flags=lanczos,split[s0][s1];[s0]palettegen=stats_mode=diff[p];[s1][p]paletteuse=dither=none" -loop {loop} "{output_file}"'
)

try:
    subprocess.run(ffmpeg_command, shell=True, check=True, close_fds=False)
    print(f'Conversion complete: {output_file}')
except subprocess.CalledProcessError:
    print('Error: Conversion failed.')
