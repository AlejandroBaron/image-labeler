# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 16:21:37 2019

@author: bkiller10
"""

from PIL import Image
from os import listdir

import sys, traceback

original_dir="./unlabeled"
convert_dir="./unlabeled_jpg"


images=listdir(original_dir)
i=0

number_errors=0
number_success=0
for img in images:
    try:
        print(img)
        im = Image.open(original_dir+"/"+img)
        
    except IOError:
        print ("cannot identify image file",img)
        im.close()
        continue
    
    
    i+=1
    if not im.mode == 'RGB':
        im = im.convert('RGB')
        rgb_im = im.convert('RGB')
        rgb_im.save(convert_dir+'/img_'+str(i)+'.jpg')
    else:
        im.save(convert_dir+'/img_'+str(i)+'.jpg')    
    im.close()
    
  