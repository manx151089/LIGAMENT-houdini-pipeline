import cv2
from cvzone.PoseModule import PoseDetector

print('===start===')
path = 'D:\Tools\houdini\python\spotJog.mp4'
destination = 'D:\Tools\houdini\python\AnimationFile2.txt'
cap = cv2.VideoCapture(path)
detector = PoseDetector()
posList = []

# Get the total number of frames in the video
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Set the frame index to the last frame
cap.set(cv2.CAP_PROP_POS_FRAMES, total_frames - 1)

print("Frame Width:", int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print("Frame Height:", int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print("Total Frames:", total_frames)
print("Current Frame Index:", int(cap.get(cv2.CAP_PROP_POS_FRAMES)))

while True:
    success, img = cap.read()
    if not success:
        break  # End the loop when no more frames are available

    detector.findPose(img)
    lmList, bboxInfo = detector.findPosition(img)

    if bboxInfo:
        lmString = ''
        for lm in lmList:
            lmString += f'{lm[1]},{img.shape[0]-lm[2]},{lm[3]},'
        posList.append(lmString)
    print('frame:', len(posList))

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('s'):
        with open(destination, 'w') as f:
            f.writelines(["%s\n" % item for item in posList])

# Release resources
cap.release()
cv2.destroyAllWindows()
