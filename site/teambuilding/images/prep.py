from importlib.resources import path
import os
# import opencv


cwd = os.getcwd()
pwd = os.path.join(cwd, 'final')

print(pwd)
os.system(f'magick convert *.png -set filename:base "%[basename]" "%[filename:base].jpg')
os.system(f'magick mogrify -resize 500x500 *.jpg -strip -interlace Plane -quality 50% -sharpen 0x0.2 *.jpg')
os.system(f'magick convert *.jpg -strip -fill white -pointsize 15 -gravity South -background black -splice 0x18 -annotate +0-0 \'%f%wx%h\' -set filename:base "%[basename]" "%[filename:base].jpg')
print('graysdcale')
os.system(f'magick convert *.jpg -set colorspace Gray  ./final/a.jpg')
print('RGB')
os.system(f'magick convert ./final/*.jpg -set colorspace RGB  ./final/a.jpg')
# os.system(f'magick convert *.jpg -ordered-dither o8x8 ')