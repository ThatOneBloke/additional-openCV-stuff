import cv2

cam = cv2.VideoCapture(0)
while True:
    frame1, frame2 = cam.read()
    mirror = cv2.flip(frame1, 1)
    #this will read the video then split it into two parts. one frame is original, frame 2 is the mirror.
    cv2.imshow("mirror effect", mirror)
    if cv2.waitKey(1) == ord("q"):
        break

cam.release()

cv2.destroyAllWindows()