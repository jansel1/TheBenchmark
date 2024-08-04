import tkinter as tk
import random
import time
from fps_counter import FPSCounter

iterations = 0
fps_data = []

lowest = 0
highest = 0
average = 0

def create_objects(canvas, num_objects, easy=False):
    objects = []

    colors = ["red", "green", "blue"]

    size_xmin = 0
    size_xmax = 800

    size_ymin = 0
    size_ymax = 800

    if easy: 
        colors = ["red", "blue"]

        size_xmin = 600
        size_xmax = 600

        size_ymin = 600
        size_ymax = 600
    
    for _ in range(num_objects):
        x, y = random.randint(0, 800), random.randint(0, 600)
        size = random.randint(10, 50)

        obj = canvas.create_oval(x, y, x + size, y + size, fill=random.choice(["red", "green", "blue"]))
        objects.append(obj)

    return objects

def animate_objects(canvas, objects):
    for obj in objects:
        dx, dy = random.randint(-5, 5), random.randint(-5, 5)
        canvas.move(obj, dx, dy)

def benchmark(easy=False, objs=1000):
    root = tk.Toplevel()
    root.title("TheBenchmark - Random Ovals")
    root.resizable(False, False)
    root.iconbitmap("TheBenchmark.ico")
    
    canvas = tk.Canvas(root, width=800, height=600, bg='white')

    canvas.pack()
    canvas.focus()

    fps_counter = FPSCounter()
    objects = create_objects(canvas, objs, easy=easy)

    start_time = time.time()

    def update():
        global iterations

        iterations += 1

        animate_objects(canvas, objects)
        fps_counter.update()
        
        canvas.delete("fps")
        canvas.create_text(10, 10, anchor='nw', text=f"FPS: {fps_counter.fps} - Iteration: {iterations}", tags="fps", fill="black")

        if not fps_counter.fps == 0 : fps_data.append(fps_counter.fps)

        if not iterations > objs:
            root.after(10, update)
        else: 
            root.quit()
            root.destroy()
    
    update()

    root.mainloop()

    end_time = time.time()
    
    average = sum(fps_data) / len(fps_data)

    highest = max(fps_data)
    lowest = min(fps_data)

    ball_count = len(objects)

    return [end_time - start_time, fps_data, lowest, highest, average, ball_count]
