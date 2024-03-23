import cv2
from cvzone.PoseModule import PoseDetector
import numpy as np
import hou

print('aaaaaaa')

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
    cap = cv2.VideoCapture(path)
    detector = PoseDetector()
    posList = []
    while True:
        success, img = cap.read()
        detector.findPose(img)
        lmList, bboxInfo = detector.findPosition(img)

        
        if bboxInfo:
            lmString = ''
            for lm in lmList:
                #print(lm)
                lmString += f'{lm[1]},{img.shape[0]-lm[2]},{lm[3]},'
            posList.append(lmString)
        print('frame:',len(posList))


        cv2.imshow("Image",img)
        key = cv2.waitKey(1)
        if key == ord('s'):
            #with open('AnimationFile.txt','w') as f:
            with open(destination,'w') as f:
                f.writelines(["%s\n" % item for item in posList])

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

