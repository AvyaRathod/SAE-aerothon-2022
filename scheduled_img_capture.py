import cv2
import schedule
import os


cam = cv2.VideoCapture(0)
cv2.namedWindow("camera module") # access camera module
img_counter = 0


def capture():
    path = "captured_frames/"
    global img_counter
    img_name = "opencv_frame{}.png".format(img_counter)
    cv2.imwrite(img_name, frame)
    print("screenshot taken")
    img_counter += 1


# Set up schedule before loop

schedule.every(1).seconds.do(capture) #


while True:
    ret, frame = cam.read()

    if not ret:
        print("failed to grab frame")
        break

    cv2.imshow("test", frame)
    schedule.run_pending()


    '''
    when the flight is complete and the drone returns to the start point, we have to stop the feed 
    '''
    key = cv2.waitKey(1)
    if key == (ord('q')):
        break 

cam.release()
cv2.destroyAllWindows()