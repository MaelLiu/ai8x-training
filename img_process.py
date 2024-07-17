from PIL import Image
import cv2
import numpy as np

def adjust_saturation(image, saturation_factor):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    hsv_image = hsv_image.astype('float32')
    hsv_image[:,:,1] *= saturation_factor
    hsv_image[:,:,1] = np.clip(hsv_image[:,:,1], 0, 255)
    hsv_image = hsv_image.astype('uint8')
    return cv2.cvtColor(hsv_image, cv2.COLOR_HSV2RGB)

def adjust_brightness(image, brightness_factor):
    # Brightness factor > 1 will make the image brighter
    # Brightness factor < 1 will make the image darker
    image = image.astype('float32')
    image *= brightness_factor
    image = np.clip(image, 0, 255)
    return image.astype('uint8')

# Load the HEIC file using Pillow
image_path = 'path_to_your_image.heic'  # Update the path to your HEIC image
image = Image.open(image_path)

# Resize the image
image = image.resize((80, 80), Image.ANTIALIAS)

# Convert image to numpy array for OpenCV processing
image_np = np.array(image)

# Adjust saturation (e.g., increase by 50%)
saturated_image = adjust_saturation(image_np, 1.5)

# Adjust brightness (e.g., increase brightness by 20%)
bright_image = adjust_brightness(saturated_image, 1.2)

# Convert back to PIL image to save as PNG
final_image = Image.fromarray(bright_image)

# Save the image
final_image.save('output_image.png', 'PNG')

print("Image processing completed and saved as 'output_image.png'")
