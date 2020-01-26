#!/usr/bin/env python

import os
import time
import shutil
from glob import iglob


    
def yyyy_mm(unix_time):
    return time.strftime("%Y_%m_%d %H:%M:%S", time.gmtime(unix_time)).split()[0][:7]

pathname = "/Users/pablo/Downloads/"
# import sys
# pathname = str(sys.argv[1])


folder_dict = { "pdf":["pdf"],\
                "music":["mp3","wav"],\
                "images":["png","dng,""jpg","HEIC","svg","eps","jpeg"],\
                "videos":["mov","mp4"],\
                "code":["sh","py","m"],\
                "application_installers":["dmg"],\
                "spreadsheets":["xlsx","csv","xls"],\
                "powerpoint":["pptx","potx","ppt"],\
                "word" : ["doc","docx","dotx"],\
                "text_files" : ["txt","md"],\
                "download_incomplete": ["download"],\
                "compressed": ["tar","zip","gz","7z"]
                
              }

year_month_today = yyyy_mm(time.time())


for filepath in iglob(f"{pathname}*.*"):
    filename = filepath[len(pathname):]
    if filename.startswith("~$"):
        continue
    ext = filename.rpartition('.')[-1]
    print(filepath)
    print(filename)
    print(ext)
    year_month_downloaded = yyyy_mm(os.path.getmtime(filepath))
    
    if year_month_downloaded == year_month_today:
        continue

    for folder in folder_dict:
        if ext.lower() in folder_dict[folder]:
            folder_path = pathname+folder+"/"+year_month_downloaded+"/"
            os.makedirs(folder_path,exist_ok=True)
            print(f"made directory {folder_path} due to {filepath} : {yyyy_mm(os.path.getmtime(filepath))} ")
            shutil.move(src=filepath,dst=folder_path+filename)
            break



