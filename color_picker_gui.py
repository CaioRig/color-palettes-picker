import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*rgb)


class ColorPickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎨 Image Color Picker")

        self.color_label = tk.Label(
            self.root, text="Click an image to get color", font=("Arial", 14)
        )

        self.canvas = tk.Canvas(self.root)
        self.canvas.pack()
        self.color_label.pack(pady=10)

        self.preview = tk.Label(
            self.root, width=10, height=2, bg="white", relief="solid"
        )
        self.preview.pack(pady=5)

        self.clipboard_label = tk.Label(
            self.root, text="", font=("Arial", 10), fg="green"
        )
        self.clipboard_label.pack(pady=5)

        self.load_button = tk.Button(
            self.root, text="🖼️ Load Image", command=self.load_image
        )
        self.load_button.pack(pady=10)

        self.image = None
        self.photo = None

    def load_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Images", "*.png *.jpg *.jpeg *.bmp")]
        )
        if not file_path:
            return

        self.image = Image.open(file_path).convert("RGB")
        self.photo = ImageTk.PhotoImage(self.image)

        self.canvas.config(width=self.image.width, height=self.image.height)
        self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        self.canvas.bind("<Button-1>", self.get_color)

    def get_color(self, event):
        if not self.image:
            return
        x, y = event.x, event.y
        rgb = self.image.getpixel((x, y))
        hex_color = rgb_to_hex(rgb)
        self.color_label.config(text=f"RGB: {rgb} | HEX: {hex_color}")
        self.preview.config(bg=hex_color)

        # Copy to clipboard
        self.root.clipboard_clear()
        self.root.clipboard_append(hex_color)
        self.root.update()

        self.clipboard_label.config(text=f"Copied {hex_color} to clipboard!")


if __name__ == "__main__":
    root = tk.Tk()
    app = ColorPickerApp(root)
    root.mainloop()
