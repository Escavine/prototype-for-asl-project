import tkinter as tk
from tkinter import messagebox
from subprocess import call

# create a function to open the HDM.py file
def open_HDM():
    call(["python", "HDM.py"])

# create the GUI window
window = tk.Tk()
window.title("ASL Project GUI (prototype)")
window.geometry("500x500")

# create the label
label = tk.Label(window, text="ASL Project GUI (prototype)", font=("Arial Bold", 20))
label.pack(pady=20)

# create the "Enter" button
enter_button = tk.Button(window, text="Enter", fg="white", bg="green", font=("Arial", 16), command=open_HDM)
enter_button.pack(pady=20)

# create the "Exit" button
def exit_program():
    if tk.messagebox.askyesno("Exit", "Are you sure you want to leave the program?"):
        window.destroy()

exit_button = tk.Button(window, text="Exit", fg="white", bg="red", font=("Arial", 16), command=exit_program)
exit_button.pack(pady=20)

# start the GUI event loop
window.mainloop()