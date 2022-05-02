import glob
import os
import shutil
import argparse
import time

from video2images import Video2Images

# Define and parse input arguments
parser = argparse.ArgumentParser()
parser.add_argument("--videos_path", type=str, default=".")
parser.add_argument("--output_path", type=str, default="images")
parser.add_argument("--capture_interval", type=int, default=1)
args = parser.parse_args()


def main():
    path = args.videos_path
    ext = '*.mp4'
    videos = glob.glob(path + '/' + ext)

    isExist = os.path.exists('frames_cropped')
    if not isExist:
        os.mkdir('frames_cropped')

    for video in videos:
        print(f"Extrayendo de {video}")
        Video2Images(video_filepath=video, capture_rate=1, out_dir="frames_cropped")
        time.sleep(1)
    
    # Select directories whit images
    subfolders = [f.path for f in os.scandir('frames_cropped') if f.is_dir()]
    paths = [f for f in subfolders if f.startswith('frames')]

    cont = 1
    isExist = os.path.exists('images')
    if not isExist:
        os.mkdir('images')

    for path in paths:
        all_images = os.listdir(path)
        for f in all_images:
            if cont % args.capture_interval == 0:
                os.rename(path + '/' + f, "images/" + f'image_{cont}.jpg')
            cont += 1
    shutil.rmtree("frames_cropped")

if __name__ == '__main__':
    main()