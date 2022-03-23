
import subprocess
import random
import os
import argparse

parser = argparse.ArgumentParser(description="set the size and color of the header pictures you want to process. example = python process.py -r 100 -c blue")
parser.add_argument('-r', '--resolution',type=int, required=True, metavar='', help="the resolution of the images ex -r 30")
parser.add_argument('-c', '--color', type=str, required=True, metavar='', help='the color tint of the images ex -c "rgb(90,90,255)" or -c blue')
args = parser.parse_args()


def process(max_size, color):
# make new folder for post processed files
    dir_p = "header_processed"
    pwd = os.getcwd()
    path_p = os.path.join(pwd, dir_p)+ "\\"

    # grab images from original header 
    dir = "header"
    path = os.path.join(pwd, dir) + "\\"

    # if not already exist, make it otherwie ignore it
    if os.path.isdir(path_p) == False:
        os.mkdir(path_p)

    # resize images in imagemagick and store them in the correct folder
    subprocess.run("magick convert -resize {}^> {}*.jpg {}%d.jpg".format(max_size,path, path_p))

    os.chdir(path_p)
    n_files = len(os.listdir(path_p))

    for i in range(n_files):
        # change the tint for every iteration
        tint = int(random.random() * 100)
        subprocess.run("magick convert {}.jpg   -colorspace gray -fill {} -tint \"{}\" -ordered-dither o8x8 {}.jpg".format(i,color,tint,i))

    # change back to orignal dir
    os.chdir(pwd)
    

if __name__=="__main__":
    process(args.resolution, str(args.color))



