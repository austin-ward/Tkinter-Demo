import random
import tkinter as tk

root = tk.Tk()
root.title("Canvas with Moving Circle")
root.geometry("800x600")

label = tk.Label(root, text="Hello Tkinter!")
label.pack()

canvas = tk.Canvas(root, width=600, height=450, bg="lightgray")
canvas.pack(pady=40)

target_radius = 10
target = canvas.create_oval(
    100 - target_radius, 100 - target_radius,
    100 + target_radius, 100 + target_radius,
    fill="red", outline=""
)


def on_click(event):
    # Move circle to a new random location within the canvas after click
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()

    max_x = canvas_width - target_radius
    max_y = canvas_height - target_radius
    new_x = random.randint(target_radius, max_x)
    new_y = random.randint(target_radius, max_y)
    canvas.coords(
        target,
        new_x - target_radius,
        new_y - target_radius,
        new_x + target_radius,
        new_y + target_radius
    )


canvas.bind("<Button-1>", on_click)

if __name__ == "__main__":
    root.mainloop()
