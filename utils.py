from PIL import Image
import numpy as np
from sklearn.cluster import KMeans

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)

def extract_dominant_colors(image, num_colors=5):
    img = image.convert('RGB')
    img_np = np.array(img)
    pixels = img_np.reshape(-1, 3)

    kmeans = KMeans(n_clusters=num_colors, random_state=42, n_init='auto')
    kmeans.fit(pixels)
    centers = np.round(kmeans.cluster_centers_).astype(int)

    hex_colors = [rgb_to_hex(tuple(color)) for color in centers]
    return hex_colors

def sample_color_at(image, x, y):
    pixel = image.convert('RGB').getpixel((x, y))
    return rgb_to_hex(pixel)
