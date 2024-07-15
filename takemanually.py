import tkinter as tk

# Global variables
sb = None
ENR_ENTRY = None
STUDENT_ENTRY = None

# Function to show error message for empty fields
def err_screen1():
    global errsc2
    errsc2 = tk.Tk()
    errsc2.geometry("330x100")
    errsc2.title("Warning!!")
    errsc2.configure(background="snow")
    tk.Label(
        errsc2,
        text="Please enter Student & Enrollment!!!",
        fg="red",
        bg="white",
        font=("times", 16, " bold "),
    ).pack()
    tk.Button(
        errsc2,
        text="OK",
        command=errsc2.destroy,
        fg="black",
        bg="lawn green",
        width=9,
        height=1,
        activebackground="Red",
        font=("times", 15, " bold "),
    ).place(x=90, y=50)

# Function to handle filling attendance
def fill_attendance():
    global ENR_ENTRY, STUDENT_ENTRY
    ENROLLMENT = ENR_ENTRY.get().strip()  # Get and strip any leading/trailing whitespace
    STUDENT = STUDENT_ENTRY.get().strip()  # Get and strip any leading/trailing whitespace
    if ENROLLMENT == "" or STUDENT == "":
        err_screen1()
    else:
        # Logic to handle filling attendance goes here
        print(f"ENROLLMENT: {ENROLLMENT}, STUDENT: {STUDENT}")

# Function to initiate manual attendance GUI
def manually_fill():
    global sb, ENR_ENTRY, STUDENT_ENTRY
    sb = tk.Tk()
    sb.title("Enter subject name...")
    sb.geometry("580x400")
    sb.configure(background="snow")

    # Label and entry for Enrollment
    ENR = tk.Label(
        sb,
        text="Enter Enrollment",
        width=15,
        height=2,
        fg="white",
        bg="blue2",
        font=("times", 15, " bold "),
    )
    ENR.place(x=30, y=130)

    ENR_ENTRY = tk.Entry(
        sb, width=20, bg="yellow", fg="red", font=("times", 23, " bold ")
    )
    ENR_ENTRY.place(x=250, y=135)

    # Label and entry for Student Name
    STUDENT = tk.Label(
        sb,
        text="Enter Student Name",
        width=15,
        height=2,
        fg="white",
        bg="blue2",
        font=("times", 15, " bold "),
    )
    STUDENT.place(x=30, y=210)

    STUDENT_ENTRY = tk.Entry(
        sb, width=20, bg="yellow", fg="red", font=("times", 23, " bold ")
    )
    STUDENT_ENTRY.place(x=250, y=215)

    # Button to fill attendance
    fill_manual_attendance = tk.Button(
        sb,
        text="Fill Attendance",
        command=fill_attendance,
        fg="white",
        bg="deep pink",
        width=20,
        height=2,
        activebackground="Red",
        font=("times", 15, " bold "),
    )
    fill_manual_attendance.place(x=250, y=290)

    sb.mainloop()

# Main loop to start the application
if __name__ == "__main__":
    manually_fill()
