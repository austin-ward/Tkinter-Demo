import tkinter as tk

root = tk.Tk()
root.title("Canvas with Static Circle")
root.geometry("800x600")

label = tk.Label(root, text="Hello Tkinter!")
label.pack()
# Create and pack a canvas for the game area
canvas = tk.Canvas(root, width=600, height=450, bg="lightgray") 
# '.pack' positions the Canvas inside the window.

canvas.pack(pady=40)

# Placing a static circle
target_radius = 10
target = canvas.create_oval(
    100 - target_radius, 100 - target_radius,
    100 + target_radius, 100 + target_radius,
    fill="red", outline=""
)

root.mainloop()
