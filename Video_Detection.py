import cv2

face_cascade = cv2.CascadeClassifier(r"C:\Users\Ubed Shaikh\Desktop\Paleet\PythonDIP\classifiers\haarcascade_frontalface_default.xml")

# video = cv2.VideoCapture(r"C:\Users\Ubed Shaikh\Desktop\Paleet\PythonDIP\faceDetection.mp4")
video = cv2.VideoCapture(0)

# print(type(video))


check = True
while check:
    check, frame = video.read()
    bw_img = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(bw_img , scaleFactor=1.25 , minNeighbors=14)
    
    for x, y, w, h in faces:
        frame = cv2.rectangle(frame, (x,y), (x+w,y+w), (0,255,0), 3)

    cv2.imshow("Video's Frame", frame)
    key = cv2.waitKey(1)
    if(key == ord('q')):
        break

cv2.destroyAllWindows()
video.release()