import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk, ImageFilter
import time
import random
import os

def create_lut(size):
    table = []
    for r in range(size):
        for g in range(size):
            for b in range(size):
                table.append((
                    int(r * 255 / (size - 1)),
                    int(g * 255 / (size - 1)),
                    int(b * 255 / (size - 1))
                ))
    return table

def process_image(image_path):
    img_filters = [
        ImageFilter.BLUR,
        ImageFilter.CONTOUR,
        ImageFilter.DETAIL,
        ImageFilter.EDGE_ENHANCE,
        ImageFilter.EDGE_ENHANCE_MORE,
        ImageFilter.EMBOSS,
        ImageFilter.FIND_EDGES,
        ImageFilter.SMOOTH,
        ImageFilter.SMOOTH_MORE,
        ImageFilter.SHARPEN,
        ImageFilter.GaussianBlur(2),
        ImageFilter.MedianFilter(3),
        ImageFilter.UnsharpMask(radius=2, percent=150),
        ImageFilter.Color3DLUT(33, create_lut(33))
    ]

    img = Image.open(image_path)
    selected_filter = random.choice(img_filters)
    img = img.filter(selected_filter)
    return img

def resize_image(img, max_width, max_height):
    width, height = img.size
    aspect_ratio = width / height

    if width > height:
        new_width = min(width, max_width)
        new_height = int(new_width / aspect_ratio)
    else:
        new_height = min(height, max_height)
        new_width = int(new_height * aspect_ratio)
    
    return img.resize((new_width, new_height), Image.Resampling.LANCZOS)

def update_image():
    global img_index, imgs, label, start_time, img_tk

    if img_index < len(imgs):
        img_path = imgs[img_index]
        processed_img = process_image(img_path)
        processed_img = resize_image(processed_img, root.winfo_width(), root.winfo_height())
        img_tk = ImageTk.PhotoImage(processed_img)
        label.config(image=img_tk)
        label.image = img_tk
        img_index += 1
        root.after(1000, update_image)
    else:
        try:
            root.quit()
            root.destroy()
        except: pass

def benchmark():
    global imgs, img_index, root, label, start_time, img_tk

    imgs = []
    for root_dir, dirs, files in os.walk('./images/'):
        for file in files:
            imgs.append(os.path.join(root_dir, file))

    root = tk.Toplevel()
    root.title("TheBenchmark - Image Processing")
    root.geometry("750x600")
    root.iconbitmap("TheBenchmark.ico")
    
    label = Label(root)
    label.pack(expand=True, fill=tk.BOTH)

    img_index = 0
    start_time = time.time()

    root.after(10, update_image)
    root.mainloop()

    end_time = time.time()

    try:
        root.quit()
        root.destroy()
    except: pass

    print("done")
    return [end_time - start_time, len(imgs)]
