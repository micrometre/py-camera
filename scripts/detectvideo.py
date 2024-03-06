import cv2 as cv
import numpy as np

carPlatesCascade = cv.CascadeClassifier('haarcascades/haarcascade_russian_plate_number.xml')

cap = cv.VideoCapture('static/video.mp4')



def gen_frames():  # generate frame by frame from camera
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        ret, frame = cap.read()
        gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        car_plates = carPlatesCascade.detectMultiScale(gray,scaleFactor=1.2,
        minNeighbors = 5, minSize=(25,25))
        for (x,y,w,h) in car_plates:
            cv.rectangle(frame,(x,y),(x+w,y+h),(255,1,0),2)
            plate = frame[y: y+h, x:x+w]
            plate = cv.blur(plate,ksize=(20,20))
        if not ret:
            print("Can't receive (stream end?). Exiting ...")
            break
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('frame', frame)
        ret, buffer = cv.imencode('.jpg', frame)
        frame = buffer.tobytes()
        print(b'--frame\r\n'b'\r\n\r\n' + frame + b'\r\n')  
        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()
gen_frames()   