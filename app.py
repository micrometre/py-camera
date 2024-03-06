# Import necessary modules
from flask import Flask, render_template, Response, request, jsonify, redirect, url_for, send_file
import cv2

# Create a Flask app instance
app = Flask(__name__, static_url_path='/static')




def gen_frames():  # generate frame by frame from camera
    camera = cv2.VideoCapture('static/video.mp4')
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('tmp/output.avi', fourcc, 10.0, (640,  480))
    carPlatesCascade = cv2.CascadeClassifier('haarcascades/haarcascade_russian_plate_number.xml')
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 80)

    print(carPlatesCascade)
    count = 0
    while True:
        ret, frame = camera.read()
        if not ret:
            break
        else:
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            car_plates = carPlatesCascade.detectMultiScale(gray,scaleFactor=1.2,
            minNeighbors = 5, minSize=(25,25))
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route("/video")
def video():
    return send_file("./tmp/alprVideo.mp4")
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')