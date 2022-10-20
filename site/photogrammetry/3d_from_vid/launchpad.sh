# make 3d from video

extractframes=3 # extract how many frame/sec? 2?
resolution="low" # (high) high res(takes a very long time)(normal) normal res(takes a long time) or (low) low model(rather quick)?
python make_3d_from_vid.py -ef "$extractframes" -res "$resolution"

# make a turntable from model

nimages=4 # how many images/model?
version="19.0.657" # which houdini version?

wdir=`pwd`
hdir="C:\Program Files\Side Effects Software\Houdini $version"
cd "$hdir"
source houdini_setup # source houdini file so we can use hython
cd "$wdir"
hython turntable.py -n "$nimages"

# make a montage and gif in imagemagick
name="joris"
pointsize=30 # setr pointsize of text on images
python montage.py -psize "$pointsize" -res "$resolution" -n "$name"

