import os
from PIL import Image

# 📁 Input and Output folders
input_folder = "images"
output_folder = "output"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Target size (Width x Height)
new_size = (800, 600)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    try:
        img_path = os.path.join(input_folder, filename)

        # Open image
        with Image.open(img_path) as img:
            # Resize image
            img_resized = img.resize(new_size)

            # Change format to PNG (optional)
            base_name = os.path.splitext(filename)[0]
            output_path = os.path.join(output_folder, f"{base_name}.png")

            # Save resized image
            img_resized.save(output_path)
            print(f"✅ Saved {output_path}")

    except Exception as e:
        print(f"❌ Error processing {filename}: {e}")
