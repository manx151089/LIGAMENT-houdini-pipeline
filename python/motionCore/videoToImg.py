import cv2
import os
def convertMp4ToJpg(filepath="",folder="",mkdir=False):
    if folder!="" and filepath!="":
        vidcap = cv2.VideoCapture(filepath)
        if(mkdir==True):
            if os.path.exists(folder):
                pass
            else:
                os.makedirs(folder)
        success,image = vidcap.read()
        count = 0
        if folder.endswith("/"):
            pass
        else:
            folder+="/"
        while success:
            cv2.imwrite(folder+"frame%d.jpg" % count, image)     # save frame as JPEG file      
            success,image = vidcap.read()
            print('Read a new frame: ', success)
            count += 1

if __name__=="__main__":
    convertMp4ToJpg("D:/Tools/houdini/python/spotJog.mp4","D:/test_output") 