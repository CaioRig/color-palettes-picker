from utils import extract_dominant_colors, sample_color_at
from PIL import Image

# Load your image
image_path = "logo.png"
image = Image.open(image_path)

# Extract dominant colors
print("🎨 Dominant Colors:")
hex_colors = extract_dominant_colors(image, num_colors=5)
for i, color in enumerate(hex_colors, 1):
    print(f"{i}. {color}")

# Sample a pixel manually
x, y = 50, 50  # Change this to any coordinate
print(f"\n🎯 Color at pixel ({x},{y}): {sample_color_at(image, x, y)}")
