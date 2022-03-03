import cv2
import os
from PIL import Image
import matplotlib.pyplot as plt
import glob
import numpy as np

for image in glob.glob("/home/mitho/Documents/ibtehaj_1/painting-animation/bg_remover/mask/*.png"):
    img=Image.open(image).convert("RGBA")
    # cv2.imwrite("h.png",img)
    img=np.array(img)
    # np.where(np.al(img  [0,0,0], axis=2))=[255,255,255]
    l,m=np.where(np.all(img <= [230,230,230,255], axis=2))
    image=os.path.basename(image)
    image=os.path.splitext(image)[0]
    imag="/home/mitho/Documents/ibtehaj_1/painting-animation/bg_remover/input_image/"+image+".jpg"
    imag= Image.open(imag).convert("RGBA")
    
    imag=np.array(imag)
    #print(imag)
    #for alpho 0
    #imag[l,m]=[0,0,0,0]
    #for white background
    imag[l,m]=[255,255,255,255]
    #print(imag)
    imag=Image.fromarray(imag)
    imag = imag.crop(imag.getbbox())
    name=os.path.basename(image)
    name=os.path.splitext(name)[0]
    #cv2.imwrite("/home/mitho/Documents/ibtehaj_1/painting-animation/bg_remover/Alpha0/"+name+".png", imag)
    imag.save("Alpha0/"+name+'.png')
    imag.save("white_bg/"+name+'.png')
