import customtkinter as ctk
import tkinter as tk

import fps_counter
import animated_balls
import physics
import img_benchmark

class App:
    def __init__(self):
        self.geo = "250x200"
        self.title = "TheBenchmark"

        self.root = tk.Tk()

        self.score = 0

        self.root.title(self.title)
        self.root.geometry(self.geo)
        self.root.resizable(False, False)
        self.root.iconbitmap("TheBenchmark.ico")

        self.root.configure(background="#242424")
        
        self.Elements()

        self.root.mainloop()

    def Elements(self):
        root = self.root

        self.ncontainer = ctk.CTkFrame(root, width=90, height=90)
        self.ncontainer.pack(fill="x")

        self.label = ctk.CTkLabel(self.ncontainer, text="Do you want to start benchmarking?")
        self.label.pack()

        self.prompt = ctk.CTkButton(self.ncontainer, text="Yes", cursor="hand2", command=self.StartBenchmark)
        self.prompt.pack()

    def update_results(self, text):
         self.results.configure(state="normal")
         self.results.insert(tk.END, text)
         self.results.configure(state="disabled")

    def StartBenchmark(self):
        self.ncontainer.destroy()

        self.root.geometry("550x550")

        self.container = ctk.CTkFrame(self.root)
        self.container.pack(fill="both", expand=True)

        self.results = ctk.CTkTextbox(self.container)
        self.results.pack(fill="both", expand=True)

        self.results.configure(state="disabled")
        self.final_result = 0

        ANIMATED_BALLS = animated_balls.benchmark()
        self.update_results(f"[Animated Balls Benchmark] ({ANIMATED_BALLS[5]} Iterations)\n\n\t[Time Taken] ({ANIMATED_BALLS[0]})\n\t[Avg. FPS] ({ANIMATED_BALLS[4]})\n\t[Lowest/Highest FPS] ({ANIMATED_BALLS[2]})/({ANIMATED_BALLS[3]})\n\n")

        IMAGE_FILTERS = img_benchmark.benchmark()
        self.update_results(f"[Image Filters Benchmark] ({IMAGE_FILTERS[1]} Images)\n\n\t[Time Taken] ({IMAGE_FILTERS[0]})\n\n")

        PHYSICS = physics.benchmark()
        self.update_results(f"[Physic Balls] ({PHYSICS[5]} Iterations)\n\t[Time Taken] ({PHYSICS[0]})\n\t[Avg. FPS] ({PHYSICS[4]})\n\t[Lowest/Highest FPS] ({PHYSICS[2]}/{PHYSICS[3]})\n\n")

        self.final_result += ANIMATED_BALLS[5] + IMAGE_FILTERS[1] + PHYSICS[5]
        self.final_result -= (PHYSICS[4] + ANIMATED_BALLS[4]) - ANIMATED_BALLS[3] + PHYSICS[3]

        self.update_results(f"\n\nFinal Result: {self.final_result}")


win = App()