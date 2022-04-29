import glob
import os
import shutil

from video2images import Video2Images

def main():
    ext = '*.mp4'
    videos = glob.glob(ext)

    isExist = os.path.exists('frames_cropped')
    if not isExist:
        os.mkdir('frames_cropped')

    for video in videos:
        print(f"Extrayendo de {video}")
        Video2Images(video_filepath=video, capture_rate=1, out_dir="frames_cropped")
    
    # Select directories whit images
    subfolders = [f.path for f in os.scandir('frames_cropped') if f.is_dir()]
    print("Estos son los subfolders", subfolders)
    paths = [f for f in subfolders if f.startswith('frames')]
    print("Estos son los paths", paths)

    cont = 0
    isExist = os.path.exists('images')
    if not isExist:
        os.mkdir('images')

    for path in paths:
        all_images = os.listdir(path)
        for f in all_images:
            os.rename(path + '/' + f, "images/" + f'image_{cont}.jpg')
            cont += 1
    shutil.rmtree("frames_cropped")

if __name__ == '__main__':
    main()