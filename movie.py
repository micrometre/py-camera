import subprocess

def convert_avi_to_mp4():
    input_file = 'tmp/output.avi'
    input_arg1 = "-i"
    input_arg2 = "-c:v"
    input_arg3 = "mpeg4"
    input_arg4 = "video.mp4"
    output = subprocess.check_output(['ffmpeg', str(input_arg1), str(input_file), str(input_arg2), str(input_arg3), str(input_arg4) ])

convert_avi_to_mp4()