import numpy as np
import imageio as ii
from PIL import Image
import os
import sys

def get_file_NamePathSuffix(fileUrl):
    filepath, tmpfilename = os.path.split(fileUrl)
    shotname, extension = os.path.splitext(tmpfilename)
    return filepath, shotname, extension

f_val = open('./datasets/CIHP/list/val.txt','w')
f_id = open('./datasets/CIHP/list/val_id.txt','w')
g = os.walk('./datasets/CIHP/images')
for path, d, filelist in g:
    for filename in filelist:
        if filename.endswith('jpg'):
            img_path = os.path.join(path, filename)
            filepath,fileshortname,filesuffix = get_file_NamePathSuffix(img_path)
            nxb_img = Image.open(img_path) # This is your image.
            # Reshape their label image to our size
            label_img = Image.open('./datasets/CIHP/labels/0005008.png') # This is the label image from CIHP.
            nxb_label_img = label_img.resize(nxb_img.size, Image.NEAREST)
            nxb_label_img.save('datasets/CIHP/labels/'+fileshortname+'.png')
            # Reshape their edge image to our size
            edge_img = Image.open('./datasets/CIHP/edges/0005008.png')
            nxb_edge_img = edge_img.resize(nxb_img.size, Image.NEAREST)
            nxb_edge_img.save('./datasets/CIHP/edges/'+fileshortname+'.png')

            f_id.write(fileshortname+'\n')
            f_val.write('/images/'+fileshortname+'.jpg /labels/'+fileshortname+'.png'+'\n' )

f_val.close()
f_id.close()

           