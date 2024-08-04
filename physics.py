import tkinter as tk
import random
import fps_counter, time

iterations = 0
fps_data = []

lowest = 0
highest = 0
average = 0

class Particle:
    def __init__(self, canvas):
        self.canvas = canvas
        self.size = random.randint(2, 5)
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 600)
        self.dx = random.choice([-1, 1]) * random.uniform(1, 3)
        self.dy = random.choice([-1, 1]) * random.uniform(1, 3)
        self.shape = canvas.create_oval(self.x, self.y, self.x + self.size, self.y + self.size, fill="blue")

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.canvas.move(self.shape, self.dx, self.dy)
        if self.x <= 0 or self.x >= 800 - self.size:
            self.dx *= -1
        if self.y <= 0 or self.y >= 600 - self.size:
            self.dy *= -1

def benchmark():
    root = tk.Toplevel()
    root.title("TheBenchmark - Particles")
    root.iconbitmap("TheBenchmark.ico")
    
    canvas = tk.Canvas(root, width=800, height=600, bg='white')
    canvas.pack()

    particles = [Particle(canvas) for _ in range(1200)]

    fps = fps_counter.FPSCounter()

    def update():
        global iterations

        fps.update()

        canvas.delete("fps")
        canvas.create_text(10, 10, anchor='nw', text=f"FPS: {fps.fps} - Iteration: {iterations}", tags="fps", fill="black")

        if not fps.fps == 0: fps_data.append(fps.fps)

        for particle in particles:
            particle.move()

        root.after(16, update)

        iterations += 1

        if iterations > 1200:
            try:
                root.quit()
                root.destroy()
            except: pass

    start_time = time.time()

    update()
    root.mainloop()

    end_time = time.time()

    highest = max(fps_data)
    lowest = min(fps_data)
    average = average = sum(fps_data) / len(fps_data)

    return [end_time - start_time, fps_data, lowest, highest, average, 1200]