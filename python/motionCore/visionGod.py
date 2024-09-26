print("===welcome to visionGod===")

import cv2
from cvzone.PoseModule import PoseDetector
import numpy as np
import hou

def openCvMotionCap(path,destination):
    """
    openCvMotionCap(path,destination)
    
    path: the path to mp4 file to capture motion from
    destination file: target file path to save the animation file in

    usage example:
    path = 'D:\Tools\houdini\python\spotJog.mp4'
    destination= 'D:\Tools\houdini\python\AnimationFile.txt'
    openCvMotionCap(path,destination)
    """
    print('===start===')
    #path = 'D:\Tools\houdini\python\spotJog.mp4'
    #destination = 'D:\Tools\houdini\python\AnimationFile3.txt'
    cap = cv2.VideoCapture(path)
    detector = PoseDetector()
    posList = []
    
    # Get total frames
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    #total_frames = 5 #overriding to debug
    # Set the frame index to the first frame
    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    print("Total Frames:", total_frames)
    
    # Create a font for the text overlay
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.8
    font_color = (255, 255, 255)  # White color
    thickness = 2
    
    while True:
        success, img = cap.read()
        if not success:
            break  # End the loop when no more frames are available
    
        detector.findPose(img)
        lmList, bboxInfo = detector.findPosition(img)
    
        if bboxInfo:
            lmString = ''
            for lm in lmList:
                #print('lm[1]:',lm[0])
                #print('img.shape[0]',img.shape[0])
                #print('lm:',lm)
                #print(lm[1],lm[2])#this  line errors out
                lmString += f'{lm[0]},{img.shape[0]-lm[1]},{lm[2]},'#need to test this line I tweaked to be lm[0-2] from lm[1-3]
            posList.append(lmString)
        curFrame = len(posList)
        print('frame:', curFrame)
    
        # Add the text overlay
        cv2.putText(img, "Press 1 to interrupt writing of frames", (20, 40), font, font_scale, font_color, thickness)
        cv2.putText(img, 'Frame:'+str(curFrame), (20, 100), font, font_scale, font_color, thickness)
        cv2.imshow("Image", img)
        key = cv2.waitKey(1)
        if curFrame == total_frames:
            key = ord('s')
        if key == ord('s'):
            with open(destination, 'w') as f:
                f.writelines(["%s\n" % item for item in posList])
                break
    
    # Release resources
    cap.release()
    cv2.destroyAllWindows()


def makeOpenCvPoints(path):
    """
    makeOpenCvPoints(str path)
    This will let the user create openCvPoints in a python sop.

    path: The path to the .txt file having the point data from openCv to create points in houdini.

    With the output of openCVMotionCap it will output an animation file
    example usage in a python sop:
    path = 'D:/Tools/houdini/python/AnimationFile.txt'
    makeOpenCvPoints(path)
    """
    
    node = hou.pwd()
    geo = node.geometry()
    
    file = hou.readFile(path)
    frames = file.split('\n')
    iFrame = int(hou.frame())
    frame = frames[iFrame]
    positions = [int(x) for x in frame.split(',')[:-1]]
    positions = np.asarray(positions)
    myLength = len(positions)/3
    posArray = np.split(positions,myLength)
    scale = np.asarray([0.01,0.01,0.005])
    posArray = [np.multiply(x,scale) for x in posArray]
    
    
    listPosArray = [x.tolist() for x in posArray]
    
    geo.clear()
    geo.createPoints(listPosArray)
    
