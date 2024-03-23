import cv2
from cvzone.PoseModule import PoseDetector

print('===start===')
path = 'D:\Tools\houdini\python\spotJog.mp4'
destination = 'D:\Tools\houdini\python\AnimationFile2.txt'
cap = cv2.VideoCapture(path)
detector = PoseDetector()
posList = []

# Get total frames
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

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
            lmString += f'{lm[1]},{img.shape[0]-lm[2]},{lm[3]},'
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

# Release resources
cap.release()
cv2.destroyAllWindows()
