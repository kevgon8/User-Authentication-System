import hashlib
import tkinter as tk
import ttkbootstrap as ttk
from tkinter import messagebox
import csv

usr_db = "usrs.csv"
session = {"active": False, "username": None}

def hash_password(psswrd):
    hashed_psswrd = hashlib.sha256(psswrd.encode()).hexdigest()
    return hashed_psswrd

def log_usr(usrnme, psswrd):
    hashed_psswrd = hash_password(psswrd)
    with open(usr_db, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if usrnme == row["username"]:
                if hashed_psswrd == row["password"]:
                    session["active"] = True
                    session["username"] == usrnme
                    usrnme_var.set("")
                    psswrd_var.set("")
                    return "Login successful! :)"
                else:
                    return "Incorrect password :("
        
        return "Incorrect username or password :("

def reg_usr(usrnme, psswrd):
    if usrnme == "" or psswrd == "":
        return "Username or passwrod cannot be empty >_<"

    hashed_psswrd = hash_password(psswrd)

    with open(usr_db, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if (usrnme == row["username"]) and (hashed_psswrd == row["password"]):
                return "User already exists >_<"

    with open(usr_db, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["username", "password"])

        writer.writerow({"username": usrnme, "password": hashed_psswrd})

    usrnme_var.set("")
    psswrd_var.set("")
    return "Registered successfully! :)"

def logout_usr():
    if session["active"] == True:
        session["active"] = False
        session["username"] = None
        return "Logged out successfully! Goodbye! :)"
    else:
        return "You haven't logged in >_<"

#GUI
window = ttk.Window(themename="cyborg")
window.title("USER AUTHENTICATION SYSTEM | NSCC SRM TASK | RA2411026010436")
window.geometry("600x485")

main_label = ttk.Label(master=window, text="User Authentication System", font="Calibri 20 bold")
main_label.pack(pady=40)

def handle_login(usrnme, psswrd):
    messagebox.showinfo("Login alert!", log_usr(usrnme.rstrip(), psswrd.rstrip()))

def handle_reg(usrnme, psswrd):
    messagebox.showinfo("Registeration alter!", reg_usr(usrnme.rstrip(), psswrd.rstrip()))

def handle_logout():
    messagebox.showinfo("Logit alert!", logout_usr())

pg1_frame = tk.Frame(master=window, width="300", height="200", borderwidth=4, relief=tk.GROOVE)
pg1_frame.propagate(False)

entry1_frame = tk.Frame(master=pg1_frame, relief=tk.GROOVE)
entry2_frame = tk.Frame(master=pg1_frame, relief=tk.GROOVE)
bttn_frame = tk.Frame(master=pg1_frame, relief=tk.GROOVE)

usrnme_var = tk.StringVar()
usrnme_field = ttk.Entry(master=entry1_frame, textvariable=usrnme_var)
label1 = ttk.Label(master=entry1_frame, text="Username: ")

psswrd_var = tk.StringVar()
psswrd_field = ttk.Entry(master=entry2_frame, textvariable=psswrd_var)
label2 = ttk.Label(master=entry2_frame, text="Password: ")

log_bttn = ttk.Button(master=bttn_frame, text="LOGIN", command=lambda: handle_login(usrnme_var.get(), psswrd_var.get()))
reg_bttn = ttk.Button(master=bttn_frame, text="REGISTER", command=lambda: handle_reg(usrnme_var.get(), psswrd_var.get()))
logout_bttn = ttk.Button(master=bttn_frame, text="LOGOUT", command=handle_logout)

entry1_frame.pack(pady=10)
label1.pack(side="left")
usrnme_field.pack(side="right")

entry2_frame.pack(pady=10)
label2.pack(side="left")
psswrd_field.pack(side="right")

bttn_frame.pack(pady=5)
log_bttn.pack(side="left", padx=3)
reg_bttn.pack(side="left", padx=3)
logout_bttn.pack(side="left", padx=3)

pg1_frame.pack()


window.mainloop()
