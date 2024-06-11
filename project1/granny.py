import tkinter
import random
import os
from PIL import Image, ImageTk


root = tkinter.Tk()
root.title("Slappin' the Granny")
root.geometry("400x300")

slapCounter = 0

def slapFunction():
    global slapCounter
    slapCounter += 1
    labelCount.config(text=f"Slaps: {slapCounter}")
    display_random_image()

def display_random_image():
    global image_label
    try:
        random_image = random.choice(image_files)  # Select a random image
        img = Image.open(random_image)
        img = img.resize((200, 200), Image.Resampling.LANCZOS)  # Resize the image
        img = ImageTk.PhotoImage(img)
        image_label.config(image=img) # type: ignore  # noqa
        image_label.image = img # type: ignore  # noqa
    except FileNotFoundError:
        error_label = tkinter.Label(root, text="No image found")
        error_label.pack_forget()  # Remove any existing error label
        error_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # type: ignore
        root.after(3000, error_label.destroy)

image_dir = os.path.dirname(os.path.abspath(__file__))
image_files = [os.path.join(image_dir, file) for file in os.listdir(image_dir) if file.endswith(('png', 'jpg', 'jpeg'))]


#Buttons
buttonSlap = tkinter.Button(text="Slap Granny", command=slapFunction)
buttonSlap.pack(pady=5)

labelCount = tkinter.Label(text=f"Slaps: {slapCounter}")
labelCount.pack(pady=5)

image_label = tkinter.Label(root)
image_label.pack(pady=10)

root.mainloop()