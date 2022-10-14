import os
import subprocess
import argparse

parser = argparse.ArgumentParser(description='make an image mosaic')
parser.add_argument('-psize', '--pointsize', type=int, metavar='', required=True, help='the pointsize of the mosaic')
parser.add_argument('-res', '--resolution', type=str, metavar='', required=True, help='resolution of the model')
parser.add_argument('-n', '--name', type=str, metavar='', required=True, help='name of the creator')
args = parser.parse_args()

def make_mosaic(pointsize, resolution, name):
    
   
    os.chdir(os.path.join(os.getcwd(),"renders") )
    call = f"magick montage -label \"%f\"  -pointsize {pointsize} -background black -fill white -geometry \"+0+0\" tile=4x3 -sharpen 0x1 -gravity South -annotate +0-0 {resolution}\" resolution\"  -gravity South  -annotate +0+{pointsize}  \" creator: \"{name}  *.jpg ../montage.png"
    result = subprocess.run(call, capture_output=True, text=True, shell=True)


if __name__=="__main__":
    make_mosaic(args.pointsize, args.resolution, args.name)

