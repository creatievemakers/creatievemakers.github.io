from importlib.resources import path
import os
# import opencv


cwd = os.getcwd()
pwd = os.path.join(cwd, 'final')

# print(pwd)


# os.system(f'magick convert *.jpg -strip -fill white -pointsize 15 -gravity North-west -background black -splice 0x50 -annotate +0-0 \'%f\\n%wx%h\\n%m\' -set filename:base "%[basename]" "%[filename:base].jpg')


# print('graysdcale')
# os.system(f'magick convert *.jpg -set colorspace Gray  ./final/a.jpg')
# print('RGB')
# os.system(f'magick convert ./final/*.jpg -set colorspace RGB  ./final/a.jpg')

print('convert png to jpg')
os.system(f'magick convert *.png -set filename:base "%[basename]" "%[filename:base].jpg')

print('convert tiff to jpg')
os.system(f'magick convert *.tiff -set filename:base "%[basename]" "%[filename:base].jpg')

print('convert jpeg to jpg')
os.system(f'magick convert *.jpeg -set filename:base "%[basename]" "%[filename:base].jpg')

print('exif')
os.system(f'magick convert -resize 500x500 ./*.jpg -quality 50% -sharpen 0x0.2 -set colorspace Gray -strip -fill white -pointsize 15 -gravity North-west -background black -splice 0x180 -annotate +0-0 \'%f\\n%wx%h\\n%[EXIF:Model]\\n%[EXIF:DateTime]\\n\\n\\n\\n\\n\\nSense_Adapt_Create%[EXIF:GPSLongitude] -fill blue -pointsize 20 -gravity South-West  -annotate +0-0 [%[p]]  ./final/a.jpg  ')
