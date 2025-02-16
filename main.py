import tkinter as tk
from tkinter import messagebox
from addcriminal import AddCriminal
from detectcriminals import DetectCriminals
def add_criminal_details():
    AddCriminal().addCriminal()

def detect_criminals():
    DetectCriminals().start_detection()
# Create the main window
root = tk.Tk()
root.title("Criminal Detection System")

# Create and pack the widgets
criminal_detection_label = tk.Label(root, text="Criminal Detection", font=("Helvetica", 16))
criminal_detection_label.pack(pady=10)

# Placeholder image, replace with your actual image
criminal_image = tk.PhotoImage(file="criminal.png")
criminal_image = criminal_image.subsample(1, 1) 
image_label = tk.Label(root, image=criminal_image)
image_label.pack(pady=10)

add_details_button = tk.Button(root, text="Add Criminal Details", command=add_criminal_details)
add_details_button.pack(pady=5)

detect_button = tk.Button(root, text="Detect Criminal", command=detect_criminals)
detect_button.pack(pady=5)

root.mainloop()
