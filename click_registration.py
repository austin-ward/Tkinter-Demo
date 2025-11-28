import random
import tkinter as tk

root = tk.Tk()
root.title("Canvas with Moving Circle")
root.geometry("800x600")

# Game state
score = tk.IntVar(value=0)
time_left = tk.IntVar(value=0)
high_score = tk.IntVar(value=0)
total_clicks = tk.IntVar(value=0)
successful_hits = tk.IntVar(value=0)
running = {'active': False, 'timer_id': None}

# UI labels
score_label = tk.Label(root, text="Score: 0", font=("Arial", 18), bg="white")
score_label.pack()
high_score_label = tk.Label(root, text="High Score: 0", font=("Arial", 18), bg="white")
high_score_label.pack()
accuracy_label = tk.Label(root, text="Accuracy: 0%", font=("Arial", 18), bg="white")
accuracy_label.pack()
timer_label = tk.Label(root, text="Time Left: 30", font=("Arial", 18), bg="white")
timer_label.pack()

# Create and pack a canvas for the game area
canvas = tk.Canvas(root, width=600, height=450, bg="lightgray")
canvas.pack(pady=40)
# Drawing up a circle
target_radius = 10
target = canvas.create_oval(
    100 - target_radius,
    100 - target_radius,
    100 + target_radius,
    100 + target_radius,
    fill="red",
    outline=""
)

# Function to move the target
def move_target():
    # Move the circle to a random location within the canvas.
    canvas.update_idletasks()  # ensure width/height are up-to-date
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    max_x = canvas_width - target_radius
    max_y = canvas_height - target_radius
    new_x = random.randint(target_radius, max_x)
    new_y = random.randint(target_radius, max_y)
    # Update the target's position on the canvas.
    canvas.coords(
        target,
        new_x - target_radius,
        new_y - target_radius,
        new_x + target_radius,
        new_y + target_radius
    )

# Start the game function
def start_game():
    # Reset counters and mark the game as active.
    running['active'] = True
    score.set(0)
    time_left.set(30)
    total_clicks.set(0)
    successful_hits.set(0)
    accuracy_label.config(text="Accuracy: 0%")
    score_label.config(text="Score: 0")
    timer_label.config(text="Time: 30")
    move_target()

# Timer update function
def update_accuracy():
    if total_clicks.get() == 0:
        accuracy_label.config(text="Accuracy: 0%")
        return
    percent = int((successful_hits.get() / total_clicks.get()) * 100)
    accuracy_label.config(text=f"Accuracy: {percent}%")

# Click event handler
def on_click(event):
    if not running['active']:
        return
    total_clicks.set(total_clicks.get() + 1)
    x = event.x
    y = event.y
    x1, y1, x2, y2 = canvas.coords(target)
    r = (x2 - x1) / 2
    cx = x1 + r
    cy = y1 + r
    if (x - cx) ** 2 + (y - cy) ** 2 <= r ** 2:
        score.set(score.get() + 1)
        successful_hits.set(successful_hits.get() + 1)
        score_label.config(text=f"Score: {score.get()}")
    update_accuracy()
    move_target()

# Bind click event to canvas
canvas.bind("<Button-1>", on_click)

start_button = tk.Button(root, text="Start Game", font=("Arial", 16), command=start_game)
start_button.pack(pady=10)

# Start immediately so clicks work without pressing the button first
start_game()

if __name__ == "__main__":
    root.mainloop()
