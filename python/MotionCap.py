import cv2
from cvzone.PoseModule import PoseDetector

def motionCap():
    cap = cv2.VideoCapture('D:\Tools\houdini\python\spotJog.mp4')
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
            with open('AnimationFile.txt','w') as f:
                f.writelines(["%s\n" % item for item in posList])

motionCap()