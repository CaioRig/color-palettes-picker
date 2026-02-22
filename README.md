
# 🎨 Image Color Picker

A Python project for extracting and picking colors from images with both GUI and CLI interfaces.

## Features

- **GUI Color Picker**: Interactive tkinter app to click on images and get RGB/HEX values
- **Dominant Color Extraction**: Automatically extract top 5 dominant colors using K-Means clustering
- **Clipboard Support**: Automatically copy colors to clipboard
- **Pixel Sampling**: Get exact color values at specific coordinates

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### GUI Application
```bash
python color_picker_gui.py
```
Click on any loaded image to pick colors. Colors are automatically copied to clipboard.

### CLI Usage
```bash
python main.py
```
Edit the `image_path` and coordinates in `main.py` to analyze different images.

## Files

- `color_picker_gui.py` - Interactive GUI application
- `main.py` - Command-line interface
- `utils.py` - Color extraction utilities
- `requirements.txt` - Dependencies

## Requirements

- Python 3.8+
- Pillow
- scikit-learn
- numpy
# color-palettes-picker
