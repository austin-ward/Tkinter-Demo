from logging import root
import tkinter as tk
# For random target placement 
import random
# For timing the game
import time

# Wraps main GUI code in a function
def main():
    # Create the main application window
    root = tk.Tk()
    # Set window title
    root.title("Pointer Accuracy Game")
    # Set window size and background color
    root.geometry("800x600")
    root.config(bg="white")
    
    # Initialize the different variables
    score = tk.IntVar(value=0)
    time_left = tk.IntVar(value=0)
    high_score = tk.IntVar(value=0)
    total_clicks = tk.IntVar(value=0)
    successful_hits = tk.IntVar(value=0)
    # Game state
    running = {'active': False, 'timer_id': None} 

    # Current score
    score_label = tk.Label(root, text="Score: 0", font=("Arial", 18), bg="white")
    score_label.pack()
    # High score 
    high_score_label = tk.Label(root, text="High Score: 0", font=("Arial", 18), bg="white")
    high_score_label.pack()
    # Accuracy 
    accuracy_label = tk.Label(root, text="Accuracy: 0%", font=("Arial", 18), bg="white")
    accuracy_label.pack()
    # Timer 
    timer_label = tk.Label(root, text="Time Left: 30", font=("Arial", 18), bg="white")
    timer_label.pack()



    # Function to start the game
    def start_game():
        # Avoid multiple starts
        if running['active']:
            return  
        # Reset score and time variables
        running['active'] = True
        score.set(0)
        time_left.set(30)
        total_clicks.set(0)
        successful_hits.set(0)
        accuracy_label.config(text="Accuracy: 0%")
        score_label.config(text="Score: 0")
        timer_label.config(text="Time: 30")
        # Start the timer
        update_timer() 

    # Start button
    start_button = tk.Button(root, text="Start Game", font=("Arial", 16), command=start_game)
    start_button.pack(pady=10)

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
    # Timer function
    def update_timer():
        if not running['active']:
            return
        # Get remaining time
        remaining = time_left.get()

        # Check if time is up
        if remaining <= 0:
            running['active'] = False
            # Update high score 
            if score.get() > high_score.get():
                high_score.set(score.get())
                high_score_label.config(text=f"High Score: {high_score.get()}")
            timer_label.config(text="Time's up!")
            print(f"Game Over! Final Score: {score.get()}")
            return
        # Decrement time left
        time_left.set(remaining - 1)
        timer_label.config(text=f"Time Left: {time_left.get()}")

        # Schedule the next update in 1 second
        running['timer_id'] = root.after(1000, update_timer)

    # Function to update accuracy display
    def update_accuracy():
        if total_clicks.get() == 0:
            accuracy_label.config(text="Accuracy: 0%")
            return
        # Calculate accuracy percentage
        percent = int((successful_hits.get() / total_clicks.get()) * 100)
        accuracy_label.config(text=f"Accuracy: {percent}%")

    # Function to handle mouse clicks
    def on_click(event):
        # Count every click
        total_clicks.set(total_clicks.get() + 1)
        # Get click coordinates
        x = event.x
        y = event.y
        # Check if click is within the target circle
        x1, y1, x2, y2 = canvas.coords(target)
        r = (x2 - x1) / 2
        cx = x1 + r
        cy = y1 + r
        # Determine hit or miss
        if (x - cx)**2 + (y - cy)**2 <= r**2:
            print("Hit!")
            score.set(score.get() + 1)
            successful_hits.set(successful_hits.get() + 1)
            score_label.config(text=f"Score: {score.get()}")
        else:
            print("Miss!")

        update_accuracy()

        # Move circle to new random location (always within canvas)
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()

        # Prevent circle from going out of bounds
        max_x = canvas_width - target_radius
        max_y = canvas_height - target_radius
        # Generate new random position for the target circle
        new_x = random.randint(target_radius, max_x)
        new_y = random.randint(target_radius, max_y)
        canvas.coords(
            target,
            new_x - target_radius, new_y - target_radius,
            new_x + target_radius, new_y + target_radius
        )
    # Bind mouse click event to the canvas
    canvas.bind("<Button-1>", on_click)

    # Start the Tkinter event loop
    root.mainloop()

# Entry point for the application
if __name__ == "__main__":
    main()

