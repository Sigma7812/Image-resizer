# Image-resizer
A Python script to **batch resize and convert images** using Pillow.

##  Features
- Reads all images from a folder
- Resizes to a fixed size
- Converts images to PNG format
- Saves processed images to an output folder
##  Project Structure
image_resizer_tool/
├── image_resizer.py
├── requirements.txt
├── .gitignore
├── images/ # Input images
└── output/ # Resized images

markdown
##  How to Run
1. Install dependencies:
```bash
pip install pillow
python image_resizer.py
