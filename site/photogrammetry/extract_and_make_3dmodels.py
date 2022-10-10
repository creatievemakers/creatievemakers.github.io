import os
import subprocess


cwd = os.getcwd()


# extract images from video and use them for images

# extract = "ffmpeg -i \"a.mp4\" -vf fps=3/1 \"out-%05d.jpg\""
# test = subprocess.run(extract, capture_output=True, text=True, shell=True)



# check if exists
# if exists, than ->
rc_dir = "C:\\Program Files\\Capturing Reality\\RealityCapture\\RealityCapture.exe"
# if not, than manually locate the file



iteration = 1

images = os.path.join(cwd, 'images')
obj_file = os.path.join(cwd, f'Model_{iteration}.obj')
params_file = os.path.join(cwd, 'params.xml')

call = f"\"{rc_dir}\" -addFolder \"{images}\" -align -setReconstructionRegionAuto -setReconstructionRegionAuto -mvsPreview -calculateTexture -exportModel \"Model 1\" \"{obj_file}\" \"{params_file}\" -quit"


result = subprocess.run(call, capture_output=True, text=True, shell=True)