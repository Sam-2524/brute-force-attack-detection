import tkinter as tk
from tkinter import messagebox
from auth import authenticate
from datetime import datetime

def log(status, user, ip):
    with open("login.log", "a") as f:
        f.write(f"{datetime.now()} {status} {ip} {user}\n")

def login():
    u = user.get()
    p = pwd.get()
    ip = ipaddr.get()

    result = authenticate(u, p, ip)

    if result == "success":
        log("SUCCESS", u, ip)
        messagebox.showinfo("Login", "Login Successful")
    elif result == "fail":
        log("FAIL", u, ip)
        messagebox.showerror("Login", "Login Failed")
    elif result == "attack":
        log("FAIL", u, ip)
        messagebox.showwarning("Alert", "Brute Force Attack Detected!\nIP Blocked")
    else:
        messagebox.showerror("Blocked", "IP Temporarily Blocked")

root = tk.Tk()
root.title("Brute Force Detection System")
root.geometry("400x300")

tk.Label(root, text="Secure Login", font=("Arial",14)).pack(pady=10)

user = tk.Entry(root)
pwd = tk.Entry(root, show="*")
ipaddr = tk.Entry(root)

for lbl, ent in [("Username",user),("Password",pwd),("IP Address",ipaddr)]:
    tk.Label(root,text=lbl).pack()
    ent.pack()

tk.Button(root,text="Login",command=login,bg="red",fg="white").pack(pady=15)
root.mainloop()
