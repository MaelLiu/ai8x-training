from PIL import Image, ImageOps
import cv2
import numpy as np

def adjust_saturation(image, saturation_factor):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    hsv_image = hsv_image.astype('float32')
    hsv_image[:, :, 1] *= saturation_factor
    hsv_image[:, :, 1] = np.clip(hsv_image[:, :, 1], 0, 255)
    hsv_image = hsv_image.astype('uint8')
    return cv2.cvtColor(hsv_image, cv2.COLOR_HSV2RGB)

def adjust_brightness(image, brightness_factor):
    image = image.astype('float32')
    image *= brightness_factor
    image = np.clip(image, 0, 255)
    return image.astype('uint8')

print("starting now...")
image_path = './red.jpeg'
target = image_path[2:-5]  # Assuming you're trying to strip the extension in a different manner
image = Image.open(image_path)
print("open up image")

# Resize the image using Image.Resampling.LANCZOS
image = image.resize((80, 80), Image.Resampling.LANCZOS)
print("resize to 80x80")

image_np = np.array(image)
print("convert to array")

saturated_image = adjust_saturation(image_np, 1.6)
print("adjust saturation")

bright_image = adjust_brightness(saturated_image, 1.3)
print("adjust brightness")

final_image = Image.fromarray(bright_image)
print("convert back to image")

final_image.save(f'output_{target}.png', 'PNG')
print("save to png")

print(f"Image processing completed and saved as 'output_{target}.png'")
