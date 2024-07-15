import pandas as pd
from glob import glob
import os
import tkinter as tk
import csv

def subjectchoose(text_to_speech):
    def calculate_attendance():
        Subject = tx.get()
        if Subject == "":
            t = 'Please enter the subject name.'
            text_to_speech(t)
            return
        
        attendance_folder = f"C:\\Users\\prasi\\Desktop\\FRAS\\Attendance\\{Subject}"
        os.chdir(attendance_folder)
        
        filenames = glob(os.path.join(attendance_folder, f"{Subject}*.csv"))
        if not filenames:
            t = f"No attendance data found for {Subject}."
            text_to_speech(t)
            return
        
        df = pd.concat([pd.read_csv(f) for f in filenames], ignore_index=True)
        df.fillna(0, inplace=True)
        
        df["Attendance"] = (df.iloc[:, 2:-1].mean(axis=1) * 100).round(2).astype(str) + '%'
        
        output_csv = os.path.join(attendance_folder, "attendance.csv")
        df.to_csv(output_csv, index=False)

        # Display attendance in a Tkinter window
        root = tk.Tk()
        root.title(f"Attendance of {Subject}")
        root.configure(background="black")
        
        with open(output_csv) as file:
            reader = csv.reader(file)
            r = 0
            
            for col in reader:
                c = 0
                for row in col:
                    label = tk.Label(
                        root,
                        width=10,
                        height=1,
                        fg="yellow",
                        font=("times", 15, "bold"),
                        bg="black",
                        text=row,
                        relief=tk.RIDGE,
                    )
                    label.grid(row=r, column=c)
                    c += 1
                r += 1
        
        root.mainloop()

    subject = tk.Tk()
    subject.title("Subject...")
    subject.geometry("580x320")
    subject.resizable(0, 0)
    subject.configure(background="black")

    titl = tk.Label(subject, bg="black", relief=tk.RIDGE, bd=10, font=("arial", 30))
    titl.pack(fill=tk.X)

    titl = tk.Label(
        subject,
        text="Which Subject of Attendance?",
        bg="black",
        fg="green",
        font=("arial", 25),
    )
    titl.place(x=100, y=12)

    def Attf():
        sub = tx.get()
        if sub == "":
            t = "Please enter the subject name!!!"
            text_to_speech(t)
        else:
            os.startfile(f"C:\\Users\\prasi\\Desktop\\FRAS\\Attendance\\{sub}")

    attf = tk.Button(
        subject,
        text="Check Sheets",
        command=Attf,
        bd=7,
        font=("times new roman", 15),
        bg="black",
        fg="yellow",
        height=2,
        width=10,
        relief=tk.RIDGE,
    )
    attf.place(x=360, y=170)

    sub = tk.Label(
        subject,
        text="Enter Subject",
        width=10,
        height=2,
        bg="black",
        fg="yellow",
        bd=5,
        relief=tk.RIDGE,
        font=("times new roman", 15),
    )
    sub.place(x=50, y=100)

    tx = tk.Entry(
        subject,
        width=15,
        bd=5,
        bg="black",
        fg="yellow",
        relief=tk.RIDGE,
        font=("times", 30, "bold"),
    )
    tx.place(x=190, y=100)

    fill_a = tk.Button(
        subject,
        text="View Attendance",
        command=calculate_attendance,
        bd=7,
        font=("times new roman", 15),
        bg="black",
        fg="yellow",
        height=2,
        width=12,
        relief=tk.RIDGE,
    )
    fill_a.place(x=195, y=170)

    subject.mainloop()

