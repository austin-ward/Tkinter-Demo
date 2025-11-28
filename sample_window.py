import tkinter as tk

root = tk.Tk()
root.title("My First Tkinter App")
root.geometry("800x600")

label = tk.Label(root, text="Hello Tkinter!")
label.pack()

root.mainloop()