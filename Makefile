.PHONY: run
flask_start:
	flask run --host=0.0.0.0 --debug
stream_file:
	 	vlc tmp/output.avi --sout "#duplicate{dst=std{access=http,mux=ts,dst=127.0.0.1:8080}}"
show_webcam:
	 vlc -vvv I dummy v4l2:///dev/video0 --sout '#transcode{vcodec=mp4v,acodec=none}:standard{access=http,mux=ts,dst=0.0.0.0:8080}'

install_pyTorch:
	pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu


#vlc v4l2:///dev/video0	 
#gst-launch-1.0 v4l2src ! jpegdec ! xvimagesink
#vlc -vvv v4l2:///dev/video0 '#standard{access=http,mux=ts,dst=0.0.0.0:12345}'
#gst-launch-1.0 v4l2src ! videoconvert ! videoscale ! video/x-raw, width=640, height=480, framerate=30/1 ! autovideosink
#vlc tmp/output.avi --sout "#duplicate{dst=std{access=http,mux=ts,dst=127.0.0.1:8080}}"