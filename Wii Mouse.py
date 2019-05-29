from nunchuck import nunchuck
import time 
from pynput.mouse import Button, Controller 


wii = nunchuck()
mouse = Controller()

while True:

    x = wii.joystick_x()
    y = wii.joystick_y()
    x_scaled = (x -130)*2/260
    y_scaled = (y-135)*2/270
    x_curve = int((x_scaled * abs(x_scaled))*100)
    y_curve = int((y_scaled * abs(y_scaled))*100)

    time.sleep(0.02)
    mouse.move(x_curve, y_curve)

    if wii.Button_z() = True:
        mouse.click(left,1)
    
    if wii.Button_c() = True:
        mouse.click(right,1)