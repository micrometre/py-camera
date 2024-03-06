# Import necessary modules
from flask import Flask, render_template, Response, request, jsonify, redirect, url_for
import cv2 as cv

# Create a Flask app instance
app = Flask(__name__, static_url_path='/static')



def gen_frames():  # generate frame by frame from camera
    carPlatesCascade = cv.CascadeClassifier('haarcascades/haarcascade_russian_plate_number.xml')
    cap = cv.VideoCapture("static/video.mp4")
    while True:
        # Capture frame-by-frame
        success, frame = cap.read()  # read the camera frame
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
        if not success:
            print("(stream end?). Exiting ...")
            break
        else:
            ret, buffer = cv.imencode('.jpg', frame)
            print(type(frame))
            frame = buffer.tobytes()
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result



# Route to stream video frames
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')