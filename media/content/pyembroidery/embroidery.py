import pyembroidery

node = hou.pwd()
geo = node.geometry()

# Add code to modify contents of geo.
# Use drop down menu to select examples.

pattern = pyembroidery.EmbPattern()

P_attribute = geo.findPointAttrib("P")
primitersrc = geo.iterPrims()

for prim in primitersrc:
    primpts = prim.points()
    i = 0
    for p in primpts:
        mypos = p.attribValue(P_attribute)
        if(i==0):
            pattern.add_command(pyembroidery.JUMP, mypos[0], -mypos[1])
        else:
            pattern.add_stitch_absolute(pyembroidery.STITCH, mypos[0], -mypos[1])
        i = i + 1
        
pattern.add_command(pyembroidery.END)
pyembroidery.write(pattern, hou.evalParm("output_dir")+"/embroidery.dst") 