
import os
import cv2
import matplotlib.pyplot as plt




cwd = os.getcwd()
pwd = os.path.join(cwd, 'final')

#os.system(f'magick convert ./final/*.jpg -set colorspace RGB  ./final/a.jpg')

print('convert png to jpg')
os.system(f'magick convert *.png -set filename:base "%[basename]" "%[filename:base].jpg')

print('convert tiff to jpg')
os.system(f'magick convert *.tiff -set filename:base "%[basename]" "%[filename:base].jpg')

print('convert jpeg to jpg')
os.system(f'magick convert *.jpeg -set filename:base "%[basename]" "%[filename:base].jpg')

print('convert dng to jpg')
os.system(f'magick convert *.dng -set filename:base "%[basename]" "%[filename:base].jpg')


print('convert JPG to jpg')
os.system(f'magick convert *.dng -set filename:base "%[basename]" "%[filename:base].jpg')



print('convert gif to jpg')
os.system(f'magick convert *.gif test_%05d.jpg')




print('convert HEIC to jpg')
os.system(f'magick convert *.HEIC -set filename:base "%[basename]" "%[filename:base].jpg')

print('exif')
os.system(f'magick convert -resize 500x500 ./*.jpg -quality 80% -strip -sharpen 0x0.2 -colorspace gray  -fill white -pointsize 15 -gravity North-west -background black -splice 0x180 -annotate +0-0 \'%f\\n%wx%h\\n%[EXIF:Model]\\n%[EXIF:DateTime]\\n\\n\\n\\n\\n\\nSense_Adapt_Create%[EXIF:GPSLongitude]%[EXIF:GPSLattitude] -fill blue -pointsize 20 -gravity South-West  -annotate +0-0 [%[p]]  ./final/a.jpg  ')



print('feature detection')
os.system(f'magick convert -resize 500x500 ./*.jpg -quality 80%  -sharpen 0x0.2  ./match/a.jpg')



import cv2
import matplotlib.pyplot as plt
# %matplotlib inline

amount = 53

for i in range(0,amount):
    for j in range(0,amount):
            if(i==j):
                j = j+1
        

            i1 = cv2.imread(f'./match/a-{i}.jpg')
            i2 = cv2.imread(f'./match/a-{j}.jpg')

            img1 = cv2.cvtColor(i1, cv2.COLOR_BGR2GRAY)
            img2 = cv2.cvtColor(i2, cv2.COLOR_BGR2GRAY)

            sift = cv2.SIFT_create()

            k_1, des_1 = sift.detectAndCompute(img1,None)
            k_2, des_2 = sift.detectAndCompute(img2,None)

            bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)

            matches = bf.match(des_1,des_2)
            matches = sorted(matches, key = lambda x:x.distance)

            print(len(matches))
            color = (255,0, 0)
            if len(matches) > 900:
                img3 = cv2.drawMatches(img1, k_1, img2, k_2, matches[:50], img2, color, color, flags=4)
                # cv2.imshow('Output', img3)


                # print(type(img3))
                cv2.imwrite(f'./match/b-{i}-{j}.jpg',img3)
                cv2.waitKey(0)
                cv2.destroyAllWindows()



print('rename')
os.system(f'magick convert ./match/b-*.jpg ./match/c.jpg')

print('make montage')
os.system(f'magick montage -tile 1x200 -geometry +0+0 -background black ./match/b-*.jpg  ./final/montage.jpg')


print('montage label')
os.system(f'magick convert ./final/montage.jpg  -sharpen 0x0.8  -fill white -pointsize 15 -gravity North-west -background black -splice 0x180 -annotate +0-0 \'%f\\n%wx%h\\n%[EXIF:Model]\\n%[EXIF:DateTime]\\n\\n\\n\\n\\n\\nSense_Adapt_Create%[EXIF:GPSLongitude] -fill blue -pointsize 20 -gravity South-West  -annotate +0-0 [%[p]]  ./final/montage.jpg  ')



