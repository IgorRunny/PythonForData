from moviepy.editor import VideoFileClip
from argparse import ArgumentParser

def cut_video (input_file, output_file, start_time, end_time):
    video = VideoFileClip(input_file)

    clip = video.subclip(start_time, end_time)
    clip.write_videofile(output_file, codec="libx264")

    video.close()
    clip.close()

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("--input")
    parser.add_argument("--start", default=0)
    parser.add_argument("--end", default=-1)
    parser.add_argument("--out", default='output.mp4')

    tmp = parser.parse_args()
    inputFile = tmp.input
    startTime = tmp.start
    endTime = tmp.end
    outputFile = tmp.out

    cut_video(inputFile, outputFile, startTime, endTime)