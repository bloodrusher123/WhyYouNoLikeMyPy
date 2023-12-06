import tkinter as tk
from tkinter import *
import datetime

window = tk.Tk()
window.geometry("350x80")
window.title("Christmas Countdown Clock")
window.configure(background="black")
now = datetime.datetime.now()
target_date = datetime.datetime(now.year, 12, 25, 0, 0,0)

if now > target_date:
    target_date = datetime.datetime(now.year+1,12 ,25,0,0,0)

objLabel1 = tk.Label(window, text="Days  Hours  Minutes  Seconds", font=("Helvetica bold",15,"bold"),fg="white",bg="black")
objLabel1.pack()
objLabel2 = tk.Label(window)
objLabel2.pack()

def update_clock():
    difference = target_date - datetime.datetime.now()

    days = difference.days
    hours = difference.seconds//3600
    minutes = (difference.seconds//60) % 60
    seconds = difference.seconds % 60

    objLabel2.config(
        text=f"{days} : {hours} : {minutes} : {seconds} ",
        font=("Helvetica bold",30, "bold")
        ,fg="white"
        ,bg="black"
        )
    window.after(1000, update_clock)

update_clock()
window.mainloop()