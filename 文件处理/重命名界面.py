"""
@time : 2025/1/26 20:08
@auth : HuZhenyuan
@file : 重命名界面.py
"""
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk


class ImageRenamerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PNG Image Renamer")
        self.root.geometry("700x600")  # 增大界面尺寸

        # Initialize the list of images
        self.image_files = []
        self.current_image_index = 0
        self.folder_path = ""  # 存储当前选择的文件夹路径

        # Frame to display the current image
        self.image_frame = tk.Frame(root)
        self.image_frame.pack(pady=10)

        # Label to show the current image name
        self.image_label = tk.Label(self.image_frame, text="Current Image: None", font=("Arial", 14))
        self.image_label.pack()

        # Canvas to display the image
        self.canvas = tk.Canvas(self.image_frame, width=300, height=300)
        self.canvas.pack()

        # Entry box for new image name
        self.name_entry = tk.Entry(root, width=40, font=("Arial", 12))
        self.name_entry.pack(pady=10)

        # Frame for the buttons (# and 0-9)
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        # Create the number buttons (0-9)
        self.buttons = []
        for i in range(10):
            button = tk.Button(self.button_frame, text=str(i), command=lambda i=i: self.append_char(str(i)), width=5,
                               height=2, font=("Arial", 14))
            button.grid(row=0, column=i, padx=5, pady=5)
            self.buttons.append(button)

        # Button for '#'
        self.hash_button = tk.Button(self.button_frame, text="#", command=lambda: self.append_char('#'), width=5,
                                     height=2, font=("Arial", 14))
        self.hash_button.grid(row=1, column=0, columnspan=10, padx=5, pady=5)

        # Frame for browsing and renaming buttons (horizontal)
        self.browse_rename_frame = tk.Frame(root)
        self.browse_rename_frame.pack(pady=10)

        # Button to browse folder (horizontal)
        self.browse_button = tk.Button(self.browse_rename_frame, text="Browse Folder", command=self.browse_folder,
                                       width=15, height=2, font=("Arial", 14))
        self.browse_button.grid(row=0, column=0, padx=10)

        # Button to rename image (horizontal)
        self.rename_button = tk.Button(self.browse_rename_frame, text="Rename Image", command=self.rename_image,
                                       width=15, height=2, font=("Arial", 14))
        self.rename_button.grid(row=0, column=1, padx=10)

        # Frame for navigation buttons (previous and next)
        self.navigation_frame = tk.Frame(root)
        self.navigation_frame.pack(pady=10)

        # Button for previous image
        self.prev_button = tk.Button(self.navigation_frame, text="Previous Image", command=self.prev_image, width=20,
                                     height=2, font=("Arial", 14))
        self.prev_button.grid(row=0, column=0, padx=10)

        # Button for next image
        self.next_button = tk.Button(self.navigation_frame, text="Next Image", command=self.next_image, width=20,
                                     height=2, font=("Arial", 14))
        self.next_button.grid(row=0, column=1, padx=10)

    def browse_folder(self):
        # Open folder dialog and get all PNG files
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.folder_path = folder_path  # Save the selected folder path
            self.image_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.png')]
            if not self.image_files:
                messagebox.showerror("No PNG Files", "No PNG images found in the selected folder.")
                return
            self.current_image_index = 0
            self.show_current_image()

    def show_current_image(self):
        if self.image_files:
            # Update image label text
            self.image_label.config(text=f"Current Image: {self.image_files[self.current_image_index]}")

            # Load and display the current image
            image_path = os.path.join(self.folder_path, self.image_files[self.current_image_index])
            img = Image.open(image_path)
            img.thumbnail((300, 300))  # Scale image to fit within canvas size
            img = ImageTk.PhotoImage(img)

            self.canvas.create_image(0, 0, anchor="nw", image=img)
            self.canvas.image = img  # Keep a reference to avoid garbage collection

            # Clear the entry box
            self.name_entry.delete(0, tk.END)

    def append_char(self, char):
        current_text = self.name_entry.get()
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, current_text + char)

    def rename_image(self):
        if not self.image_files:
            messagebox.showerror("No Images", "No images loaded to rename.")
            return

        # Get the new name from the entry box
        new_name = self.name_entry.get().strip()
        if not new_name:
            messagebox.showwarning("Empty Name", "Please enter a new name for the image.")
            return

        # Get the old file name and new file name
        old_file_name = self.image_files[self.current_image_index]
        new_file_name = new_name + ".png"

        # Construct the full file paths
        old_file_path = os.path.join(self.folder_path, old_file_name)
        new_file_path = os.path.join(self.folder_path, new_file_name)

        # Rename the file
        try:
            os.rename(old_file_path, new_file_path)
            self.image_files[self.current_image_index] = new_file_name
            self.current_image_index += 1
            if self.current_image_index < len(self.image_files):
                self.show_current_image()  # Show next image
            else:
                messagebox.showinfo("All Done", "All images have been renamed!")
        except Exception as e:
            messagebox.showerror("Rename Error", f"Error renaming file: {e}")

    def prev_image(self):
        # Go to the previous image
        if self.current_image_index > 0:
            self.current_image_index -= 1
            self.show_current_image()
        else:
            messagebox.showinfo("First Image", "You are already on the first image.")

    def next_image(self):
        # Go to the next image
        if self.current_image_index < len(self.image_files) - 1:
            self.current_image_index += 1
            self.show_current_image()
        else:
            messagebox.showinfo("Last Image", "You are already on the last image.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageRenamerApp(root)
    root.mainloop()

