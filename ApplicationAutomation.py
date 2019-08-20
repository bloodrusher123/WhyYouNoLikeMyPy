from pywin32 import application

import time

app = application.Application()
app.start("Notepad.exe")
time.sleep(3)
app.Notepad.edit.TypeKeys("Hello World")