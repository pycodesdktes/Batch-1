import tkinter as tk           #Tkinter module is imported
from tkinter import filedialog, Text
import os                      #functions for creating and removing a directory (folder)

root = tk.Tk()
apps = []

def addApp():                 #Adds apps/files in the list

    for widget in frame.winfo_children():
        widget.destroy()

    filename=filedialog.askopenfilename(initialdir="/", title="Select File",
                filetypes=(("executable", "*.exe"), ("all files", "*.*")))

    apps.append(filename)
    print(filename)
    for app in apps:
        lable = tk.Label(frame, text=app, bg="gray")
        lable.pack()


def runApps():       #Executes the provided apps/files
    for app in apps:
        os.startfile(app)


if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

canvas = tk.Canvas(root, height=500, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#263D42", command=runApps)
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()


root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')

