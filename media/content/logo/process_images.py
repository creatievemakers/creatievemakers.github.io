
import subprocess


subprocess.run("magick mogrify -resize 30x30! *.jpg")
subprocess.run("magick convert *.jpg -colorspace gray -fill blue -tint 100 -ordered-dither o8x8 -set filename:base \"%[basename]\" \"%[filename:base].jpg\"")


