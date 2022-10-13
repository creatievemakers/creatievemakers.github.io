import os
import subprocess

print("make montage")

   
os.chdir(os.path.join(os.getcwd(),"renders") )

call = f"magick montage -label \"%f\" -pointsize 10, -background blue, -fill red, -bordercolor black, -border 1, -geometry \"+0+0\" tile=4x3 *.png ../montage.png"

call = f"magick convert -delay 8 *.jpg animation.gif"

result = subprocess.run(call, capture_output=True, text=True, shell=True)
