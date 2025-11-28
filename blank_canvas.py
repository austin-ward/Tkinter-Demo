import tkinter as tk

root = tk.Tk()
root.title("Blank Canvas")
root.geometry("800x600")

label = tk.Label(root, text="Hello Tkinter!")
label.pack()
# Create and pack a canvas for the game area
canvas = tk.Canvas(root, width=600, height=450, bg="lightgray") 
# '.pack' positions the Canvas inside the window.

canvas.pack(pady=40)
root.mainloop()
