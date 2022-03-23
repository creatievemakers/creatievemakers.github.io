
from email import header
import subprocess
import random
import os



# make new folder for post processed files
dir_p = "header_processed"
pwd = os.getcwd()
path_p = os.path.join(pwd, dir_p)+ "\\"



# grab images from original header 
dir = "header"
path = os.path.join(pwd, dir) + "\\"
print (path_p )

# if not already exist, make it otherwie ignore it
if os.path.isdir(path_p) == False:
    os.mkdir(path_p)
    print ('y')


subprocess.run("magick convert -resize 30^> {}*.jpg {}%d.jpg".format(path, path_p))

os.chdir(path_p)
n_files = len(os.listdir(path_p))

for i in range(n_files):

    tint = int(random.random() * 100)
    subprocess.run("magick convert {}.jpg   -colorspace gray -fill rgba(80,80,255,1) -tint {} -ordered-dither o8x8 {}.jpg".format(i,tint,i))

# if __name__=="__main__":
#     process()