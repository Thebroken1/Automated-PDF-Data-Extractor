import tkinter as tk
from tkinter import filedialog

def browse_file():
    file_path = filedialog.askopenfilename(title="Select a File", 
                                           filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")])
    if file_path:  # If a file is selected
        label.config(text=f"Selected File: {file_path}")

# Create main window
root = tk.Tk()
root.title("File Browser")

# Button to browse files
button = tk.Button(root, text="Browse File", command=browse_file)
button.pack(pady=10)

# Label to show selected file
label = tk.Label(root, text="No file selected")
label.pack(pady=10)

root.mainloop()
