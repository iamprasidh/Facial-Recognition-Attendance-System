import tkinter as tk
from tkinter import *
import os
import cv2
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.font as font
import pyttsx3

# Project modules
import show_attendance
import takeImage
import trainImage
import automaticAttendance

# Initialize text-to-speech engine
engine = pyttsx3.init()

def text_to_speech(user_text):
    engine.say(user_text)
    engine.runAndWait()

# File paths
base_path = "C:\\Users\\prasi\\Desktop\\FRAS"
haarcasecade_path = os.path.join(base_path, "haarcascade_frontalface_default.xml")
trainimagelabel_path = os.path.join(base_path, "TrainingImageLabel", "Trainner.yml")
trainimage_path = os.path.join(base_path, "TrainingImage")
studentdetail_path = os.path.join(base_path, "StudentDetails", "studentdetails.csv")
attendance_path = os.path.join(base_path, "Attendance")

# Initialize main window
window = Tk()
window.title("Face Recognizer")
window.geometry("1280x720")
window.configure(background="black")

# Functions for UI elements and functionality
def del_sc1():
    sc1.destroy()

def err_screen():
    global sc1
    sc1 = tk.Tk()
    sc1.geometry("400x110")
    sc1.title("Warning!!")
    sc1.configure(background="black")
    sc1.resizable(0, 0)
    tk.Label(sc1, text="Enrollment & Name required!!!", fg="yellow", bg="black", font=("times", 20, "bold")).pack()
    tk.Button(sc1, text="OK", command=del_sc1, fg="yellow", bg="black", width=9, height=1, activebackground="Red", font=("times", 20, "bold")).place(x=110, y=50)

def testVal(inStr, acttyp):
    if acttyp == "1" and not inStr.isdigit():  # insert
        return False
    return True

# Load and display logo
logo = Image.open("UI_Image/0001.png").resize((50, 47), Image.LANCZOS)
logo1 = ImageTk.PhotoImage(logo)
titl = tk.Label(window, bg="black", relief=RIDGE, bd=10, font=("arial", 35))
titl.pack(fill=X)
tk.Label(window, image=logo1, bg="black").place(x=470, y=10)

# Title
tk.Label(window, text="Smart College!!", bg="black", fg="green", font=("arial", 27)).place(x=525, y=12)
tk.Label(window, text="Welcome to the Face Recognition Based\nAttendance Management System", bg="black", fg="yellow", bd=10, font=("arial", 35)).pack()

# Load and display images
images = {
    "register": ("UI_Image/register.png", 100, 270),
    "attendance": ("UI_Image/attendance.png", 980, 270),
    "verify": ("UI_Image/verifyy.png", 600, 270)
}

for key, (path, x, y) in images.items():
    img = Image.open(path)
    img = ImageTk.PhotoImage(img)
    label = Label(window, image=img)
    label.image = img
    label.place(x=x, y=y)

def TakeImageUI():
    ImageUI = Tk()
    ImageUI.title("Take Student Image..")
    ImageUI.geometry("780x480")
    ImageUI.configure(background="black")
    ImageUI.resizable(0, 0)
    tk.Label(ImageUI, bg="black", relief=RIDGE, bd=10, font=("arial", 35)).pack(fill=X)
    tk.Label(ImageUI, text="Register Your Face", bg="black", fg="green", font=("arial", 30)).place(x=270, y=12)
    tk.Label(ImageUI, text="Enter the details", bg="black", fg="yellow", bd=10, font=("arial", 24)).place(x=280, y=75)

    # Enrollment No
    lbl1 = tk.Label(ImageUI, text="Enrollment No", width=10, height=2, bg="black", fg="yellow", bd=5, relief=RIDGE, font=("times new roman", 12))
    lbl1.place(x=120, y=130)
    txt1 = tk.Entry(ImageUI, width=17, bd=5, validate="key", bg="black", fg="yellow", relief=RIDGE, font=("times", 25, "bold"))
    txt1.place(x=250, y=130)
    txt1["validatecommand"] = (txt1.register(testVal), "%P", "%d")

    # Name
    lbl2 = tk.Label(ImageUI, text="Name", width=10, height=2, bg="black", fg="yellow", bd=5, relief=RIDGE, font=("times new roman", 12))
    lbl2.place(x=120, y=200)
    txt2 = tk.Entry(ImageUI, width=17, bd=5, bg="black", fg="yellow", relief=RIDGE, font=("times", 25, "bold"))
    txt2.place(x=250, y=200)

    # Notification
    lbl3 = tk.Label(ImageUI, text="Notification", width=10, height=2, bg="black", fg="yellow", bd=5, relief=RIDGE, font=("times new roman", 12))
    lbl3.place(x=120, y=270)
    message = tk.Label(ImageUI, text="", width=32, height=2, bd=5, bg="black", fg="yellow", relief=RIDGE, font=("times", 12, "bold"))
    message.place(x=250, y=270)

    def take_image():
        l1 = txt1.get()
        l2 = txt2.get()
        takeImage.TakeImage(l1, l2, haarcasecade_path, trainimage_path, message, err_screen, text_to_speech)
        txt1.delete(0, "end")
        txt2.delete(0, "end")

    # Take Image button
    tk.Button(ImageUI, text="Take Image", command=take_image, bd=10, font=("times new roman", 18), bg="black", fg="yellow", height=2, width=12, relief=RIDGE).place(x=130, y=350)

    def train_image():
        trainImage.TrainImage(haarcasecade_path, trainimage_path, trainimagelabel_path, message, text_to_speech)

    # Train Image button
    tk.Button(ImageUI, text="Train Image", command=train_image, bd=10, font=("times new roman", 18), bg="black", fg="yellow", height=2, width=12, relief=RIDGE).place(x=360, y=350)

# Register new student button
tk.Button(window, text="Register a new student", command=TakeImageUI, bd=10, font=("times new roman", 16), bg="black", fg="yellow", height=2, width=17).place(x=100, y=520)

def automatic_attedance():
    automaticAttendance.subjectChoose(text_to_speech)

# Take Attendance button
tk.Button(window, text="Take Attendance", command=automatic_attedance, bd=10, font=("times new roman", 16), bg="black", fg="yellow", height=2, width=17).place(x=600, y=520)

def view_attendance():
    show_attendance.subjectchoose(text_to_speech)

# View Attendance button
tk.Button(window, text="View Attendance", command=view_attendance, bd=10, font=("times new roman", 16), bg="black", fg="yellow", height=2, width=17).place(x=1000, y=520)

# Exit button
tk.Button(window, text="EXIT", bd=10, command=quit, font=("times new roman", 16), bg="black", fg="yellow", height=2, width=17).place(x=600, y=660)

window.mainloop()
