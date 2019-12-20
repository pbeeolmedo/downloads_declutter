#!/usr/bin/env python

import os
import shutil
from glob import iglob


pathname = "/Users/pablo/Downloads/"

pdf_list = ["pdf",[".pdf"]]
music_list = ["music",[".mp3",".wav"]]
image_list = ["images",[".png",".jpg",".HEIC",".svg",".eps"]]



for filename in iglob(pathname+'*.*'):
    filename = filename[len(pathname):]
    print(filename)

    
def file_mover(ext_list,folder_name) 
    for ext in ext_list:
        if filename.endswith(ext):
            folder_path = pathname+folder_name+filename
            shutil.move(src=filename,dst=folder_path)
