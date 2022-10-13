import hou
import os
import toolutils

def render_model():

    hou.hipFile.load("empty.hipnc")
    print("empty file loaded")

    obj = hou.node("/obj")

    render = obj.createNode("geo","render")

    # get current wdir
    home_dir = os.getcwd()
    obj_dir = os.path.join(os.getcwd(), "obj")

    file_sop = render.createNode("file") 

    delete_small_parts = render.createNode("labs::delete_small_parts")
    delete_small_parts.setInput(0, file_sop)
    delete_small_parts.setParms({'bKeeplargest':1})


    transform = render.createNode("xform")
    transform.setInput(0, delete_small_parts)
    transform.setParms({'rx':-90})

    matchsize = render.createNode("matchsize")
    matchsize.setInput(0, transform)
    matchsize.setParms({'sizex':2, 'sizey':2, 'sizez':2, 'doscale':1, 'justify_y':1,})

    attrib_delete = render.createNode("attribdelete")
    attrib_delete.setInput(0, matchsize)
    attrib_delete.setParms({'ptdel':"Cd"})

    material = render.createNode("labs::quickmaterial::2.2")
    material.setInput(0, attrib_delete)

    normal = render.createNode("normal")
    normal.setInput(0, material)
    normal.setParms({'type':0})

    attribwrangle = render.createNode("attribwrangle") 
    attribwrangle.setInput(0, normal)
    attribwrangle_path = attribwrangle.path()
    
    null = render.createNode("null")
    null.setInput(0, attribwrangle)
    null_path = null.path()
    null.setDisplayFlag(True)
    null.setRenderFlag(True)

    rivet = obj.createNode("rivet")
    rivet.parm("rivetsop").set(render.path())

    rivet.setParms({'rivetgroup': f"`npoints(\"{null_path}\")-1`", 'rivetuseattribs': "1"})
    
    cam = obj.createNode("cam","cam1")
    cam.setParms({'tx':-0.5, 'resx': 720, 'resy': 720, 'rz': 90, "aperture": 41, 'projection': 1, 'orthowidth': 2.5})
    cam.setInput(0, rivet)
    
    ropnet = render.createNode("ropnet")
    
    opengl = ropnet.createNode('opengl')
    opengl.parm("gamma").set(2.2)


    for index, file in enumerate(os.listdir(obj_dir)):
           
        os.chdir(os.path.join(obj_dir, file))
        file_dir = os.getcwd()
        file_sop.setParms({'file':os.path.join(file_dir, file + ".obj")})
        material.setParms({'principledshader_basecolor_texture_1':os.path.join(file_dir, file + "_u1_v1.png")})

        v = 30 # amount of images per model
        for i in range(0, v):
            attribwrangle.setParms({'class': 0, 'snippet':
            f"""
            vector startpos = set(1,2,1);
            int cam_pnt = addpoint(0, startpos);
            float divisions = 2*PI / {v};
            int iteration = {i};
            float mult = 3;
            vector newpos = set( sin((startpos.x ) * (divisions * iteration)) * mult ,startpos.y, cos((startpos.z ) * (divisions * iteration)) * mult);

            setpointattrib(0,"P",cam_pnt, newpos,"set");
            setpointattrib(0, "N", cam_pnt, newpos, "set");
            setpointattrib(0, "up", cam_pnt, set(0,-1,0), "set");
            """
            
            })

            # make folder named rendered_images
            os.chdir(home_dir)
            render_dir = os.path.join(home_dir, 'renders')

            if os.path.exists(render_dir) == True:
                os.chdir(render_dir)
            else:
                os.chdir(home_dir)
                os.mkdir("renders")
                os.chdir(render_dir)


            opengl.setParms({'picture': f"{file}_{i}.jpg"})
            opengl.parm("execute").pressButton()


        obj.layoutChildren()
        render.layoutChildren()


    os.chdir(home_dir)
    hou.hipFile.save("turntable.hipnc")
    print("file saved") 

    
if __name__=="__main__":
    render_model()











