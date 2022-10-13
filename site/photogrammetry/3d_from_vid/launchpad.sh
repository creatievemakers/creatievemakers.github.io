# make 3d from video

# extract how many frame/sec? 2?
# hight res(takes a very long time) or preview model(rather quick)?
python "make_3d_from_vid.py"

# make a turntable from model

# which houdini version
# how many images/model?
wdir=`pwd`
hdir="C:\Program Files\Side Effects Software\Houdini 19.0.657"
cd "$hdir"
source houdini_setup 
cd "$wdir"
hython "test.py"

# make a montage and gif in imagemagick
python "montage.py"
