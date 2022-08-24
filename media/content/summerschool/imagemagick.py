import os
cwd = os.getcwd()
folder = input('enter folder you want to use with imagemagick ')
pwd = os.path.join(cwd, folder)
os.chdir(pwd)
os.system('magick mogrify -resize 1080x1080! *.jpg')
print('done')