from moviepy.editor import VideoFileClip
from pathlib import Path
from argparse import ArgumentParser
from PIL import Image
import shutil

def cut_to_frames (input_file, start_time, end_time, output_directory, step=10):
    video = VideoFileClip(input_file)

    clip = video.subclip(start_time, end_time)

    if not Path(output_directory).exists():
        Path(output_directory).mkdir()

    check_frame_width = clip.get_frame(t=1).shape[1]
    width = 250 if check_frame_width > 250 else check_frame_width

    fps = clip.fps
    frame_counter = 0

    for i, frame in enumerate(clip.iter_frames(fps=fps)):
        if int(i) % int(step) == 0:
            img = Image.fromarray(frame)
            img_resized = img.resize((width, int(width * img.height / img.width)))
            directory = Path(output_directory).joinpath(f"{frame_counter:04d}.png")
            img_resized.save(directory)
            frame_counter += 1



if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("--input")
    parser.add_argument("--start", default=0)
    parser.add_argument("--end", default=-1)
    parser.add_argument("--out", default="output")
    parser.add_argument("--step", default=10)

    tmp = parser.parse_args()
    inputFile = tmp.input
    startTime = tmp.start
    endTime = tmp.end
    outputDirectory = tmp.out
    step = tmp.step

    cut_to_frames(inputFile, startTime, endTime, outputDirectory, step)