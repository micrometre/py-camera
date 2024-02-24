.PHONY: run
flask_start:
	flask run --host=0.0.0.0 --debug

stream_vlac:
	 vlc alprVideo.mp4 --sout "#duplicate{dst=std{access=http,mux=ts,dst=127.0.0.1:8080}}"
