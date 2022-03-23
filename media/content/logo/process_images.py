
from math import floor
import subprocess
import random
import math


# subprocess.run("magick mogrify -resize 30x30! *.jpg")
# subprocess.run("magick convert *.jpg -colorspace gray -fill blue -tint 80  ./pp/%d.jpg")


# subprocess.run("magick mogrify -resize 30x30! %d.jpg")
subprocess.run("magick convert -resize 30x30! *.jpg ./pp/%d.jpg")

for i in range(6):

    tint = int(random.random() * 100)
    
    subprocess.run("magick convert -resize 30x30! ./pp/{}.jpg -colorspace gray *.jpg".format(i))
