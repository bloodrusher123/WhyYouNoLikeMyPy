from picamera import picamera
from time import sleep 
import datetime

camera = PiCamera()

camera.start_preview()
sleep(5)
camera.start_recording('/home/pi/desktop/video.h264'+datetime.now())
sleep(5)
camera.stop_recording()
camera.stop_preview()
