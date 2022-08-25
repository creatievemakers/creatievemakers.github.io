
import os
import shutil
import random

cwd = os.getcwd()
basedirectory = 'base'
montagedirectory = 'big_montage'

def change_path(id):
    os.chdir(cwd)
    pwd = os.path.join(cwd + '/' + operation[id])
    if os.path.exists(pwd)==False:
        os.mkdir(pwd)
    return pwd

def create_input(): # for every letter in the alphabet, so we have data to work with
    for x in range(0,26):
        letter = chr(x+97)    
        os.system(f'magick convert -background white -size 80x90 -gravity center -fill black -font Arial -pointsize 72 label:{letter} {letter}.jpg')
    return None

def convert(): # convert images to different formats

    pwd = change_path(0)

    os.chdir(pwd)
    os.system(f'magick convert -delay 8 {base}/*.jpg animation.gif') # make a gif from all images
    os.system(f'magick {base}/a.jpg a.png') # convert a.jpg to a.png
    return None

def resize():# resize images
    pwd = change_path(1)
    
    os.chdir(pwd)

    for image in os.listdir(base): # duplicate images
        shutil.copyfile(cwd + '/' + f'{basedirectory}/{image}', pwd + '/' + f'{image}') 

    # os.system('magick mogrify -resize 50x30! *.jpg') #resize all the same resolution. ! == do not take the original aspect ratio into account

    for image in os.listdir(pwd): # randomize the resolution
        res = str(random.randint(62, 360)) + 'x' + str(random.randint(140, 400)) + '!'
        os.system(f'magick mogrify -resize {res} {image} ')
    return None

def res_comp_sharpen(): #change resolution, compression and sharpen

    pwd = change_path(2)
    os.chdir(pwd)
    
    for image in os.listdir(base): # duplicate images
        shutil.copyfile(cwd + '/' + f'{basedirectory}/{image}', pwd + '/' + f'{image}') 

    os.system(f'magick mogrify -resize 107x129! -strip -interlace Plane -quality 1% -sharpen 0x10 *.jpg')
    return None

def label():# label images with their own metadata, and rename them

    pwd = change_path(3)

    os.chdir(pwd)
    os.system(f'magick convert  {base}/*.jpg -fill white -pointsize 5 -gravity South -background black -splice 0x18 -annotate +0-0 \'%f\\n%wx%h\' -set filename:base "%[basename]" "%[filename:base]_label.jpg"')
    return None

def montage():# make a montage
    pwd = change_path(4)

    os.chdir(pwd)
    os.system(f'magick montage -label %f -pointsize 10 -bordercolor black -border 1 -geometry +0+0 {base}/*.jpg montage.jpg') # make an image montage 
    return None

def dither():# make a montage
    pwd = change_path(5)

    os.chdir(pwd)
    os.system(f'magick convert {base}/*.jpg -blur 0x2 -ordered-dither o8x8,2 -set filename:base "%[basename]" "%[filename:base].jpg"') # make an image montage 
    return None

def edge_detection():# edge detection
    pwd = change_path(6)

    os.chdir(pwd)
    os.system(f'magick convert {base}/*.jpg -sharpen 0x15 -canny 0x1+10%+30% -set filename:base "%[basename]" "%[filename:base].jpg"') # edge detection 
    return None

def big_montage(): #make a big montage of all the images
    pwd = os.path.join(cwd + '/' + montagedirectory)
    if os.path.exists(pwd)==False:
        os.mkdir(pwd)

    for i in range(len(operation)):
        pwd = change_path(i)
        label = operation[i]
        os.chdir(pwd)
        os.system(f'magick montage  -bordercolor black -border 1 -geometry +0+0 *.jpg ../{montagedirectory}/{label}.jpg')
    return None


base = os.path.join(cwd + '/' + f'{basedirectory}')
if os.path.exists(base)==False:
        os.mkdir(base)
os.chdir(base)

operation = ["convert", "resize", "resolution_compress_sharpen", "label_images", "montage", "dither", "edge_detection"]

def inputs():
    create_input()
    return None
def operations():
    convert()
    resize()
    res_comp_sharpen()
    label()
    montage()
    dither()
    edge_detection()
    return None
def post_processing():
    big_montage()
    return None

def main():
    inputs()
    operations()
    post_processing()
    return None

if __name__ == "__main__":
    main()