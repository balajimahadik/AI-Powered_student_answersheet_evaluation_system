from inference_sdk import InferenceHTTPClient
from PIL import Image
import json
import os
from dotenv import load_dotenv

# image_path = "O:\\IPCV\\CP\\FinalCP\\static\\TestImages\\diagram2.png"

load_dotenv()

api_key = os.getenv('RoboFlow_API_KEY')

CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key=api_key
)

# result = CLIENT.infer(image_path, model_id="diagram-detection-wsnbk/1")
# print(result)
#
# image = Image.open(image_path)

# Model output in JSON format (you can replace this with actual model output if needed)
# model_output = result

# Iterate through each detection and crop the image
# for i, prediction in enumerate(model_output['predictions']):
#     # Get the bounding box for each detected object
#     x_center = prediction['x']
#     y_center = prediction['y']
#     width = prediction['width']
#     height = prediction['height']
#
#     # Calculate the bounding box coordinates
#     left = x_center - width / 2
#     top = y_center - height / 2
#     right = x_center + width / 2
#     bottom = y_center + height / 2
#
#     # Crop the image
#     cropped_image = image.crop((left, top, right, bottom))
#
#     # Convert the image to RGB mode before saving
#     cropped_image = cropped_image.convert("RGB")  # Converting to RGB to remove alpha channel
#
#     # Save the cropped image with a unique filename
#     cropped_image_path = f"cropped_image_{i}.jpg"
#     cropped_image.save(cropped_image_path)
#     print(f"Saved cropped image {i} to {cropped_image_path}")

def extractblkdig(image_path,page_num,location):
    image = Image.open(image_path)
    result = CLIENT.infer(image_path, model_id="diagram-detection-wsnbk/1")
    print(result)
    model_output = result
    # Iterate through each detection and crop the image
    i = page_num
    count = 0
    for prediction in model_output['predictions']:
        # Get the bounding box for each detected object
        x_center = prediction['x']
        y_center = prediction['y']
        width = prediction['width']
        height = prediction['height']

        # Calculate the bounding box coordinates
        left = x_center - width / 2
        top = y_center - height / 2
        right = x_center + width / 2
        bottom = y_center + height / 2

        # Crop the image
        cropped_image = image.crop((left, top, right, bottom))

        # Convert the image to RGB mode before saving
        cropped_image = cropped_image.convert("RGB")  # Converting to RGB to remove alpha channel

        # Save the cropped image with a unique filename
        cropped_image_path = f"./static/ImageData/{location}/cropped_image_{i}.png"
        cropped_image.save(cropped_image_path)
        print(f"Saved cropped image {i} to {cropped_image_path}")
        i=i+1
        count=count+1
    return count,page_num