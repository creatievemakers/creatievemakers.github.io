import os
import subprocess
import argparse

parser = argparse.ArgumentParser(description='make a 3d model from videos')
parser.add_argument('-ef', '--extractframe', type=int, metavar='', required=True, help='extract fps from videos')
parser.add_argument('-res', '--resolution', type=str, metavar='', required=True, help='resolution of the model')
args = parser.parse_args()


def make_3d(extractframe, resolution):

    cwd = os.getcwd()
    videos = 'videos'

    rc_dir = "C:\\Program Files\\Capturing Reality\\RealityCapture"
    video_dir = os.path.join(cwd, 'videos')


    if (os.path.isdir(rc_dir)==True):
        rc = os.path.join("C:\\Program Files\\Capturing Reality\\RealityCapture","RealityCapture.exe")
    else:
        rc = os.path.join(input('RealityCapture direcory: '), "RealityCapture.exe")

    if(os.path.isdir(os.path.join(cwd, 'obj'))) == False:
        os.mkdir(os.path.join(cwd, 'obj'))

    geo_dir = os.path.join(cwd, 'obj')
    images_dir = os.path.join(cwd, 'videos')



    for index,file in enumerate(os.listdir(videos)):

        if file.find(".")!=-1:

            os.chdir(os.path.join(cwd, videos))
            vid = os.path.splitext(file)[0] #videoname without extension

            obj_dir = os.path.join(geo_dir, vid)
            if os.path.isdir(obj_dir)==False: os.mkdir(obj_dir)
                

            dir = os.path.join(video_dir,vid ) #cwd + vid
            if os.path.isdir(dir) == False: os.mkdir(dir) #make folder if it does not exist yet, else ignore
                
            
            extract = f"ffmpeg -i \"{file}\" -vf fps={extractframe}/1 -qscale:v 2 \"{vid}\\{vid}-%04d.jpg\"" #fix this, no good quality

            
            images = os.path.join(images_dir, f'{vid}')
            obj_file = os.path.join(obj_dir, f'{vid}.obj')
            params_file = os.path.join(cwd, 'params.xml')

            if(resolution=="low"): res = "mvsPreview"
            if(resolution=="normal"): res = "mvs"
            if(resolution=="high"): res = "mvsHigh"
            

            call = f"\"{rc}\" -addFolder \"{images}\" -align -setReconstructionRegionAuto -setReconstructionRegionAuto -\"{res}\" -calculateTexture -exportModel \"Model 1\" \"{obj_file}\" \"{params_file}\" -quit"

            print(file)

            subprocess.run(extract, capture_output=True, text=True, shell=True)
            result = subprocess.run(call, capture_output=True, text=True, shell=True)

if __name__=="__main__":
    make_3d(args.extractframe, args.resolution)



