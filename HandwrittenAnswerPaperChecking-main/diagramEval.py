from dotenv import load_dotenv
import os
from inference_sdk import InferenceHTTPClient
from PIL import Image
import json
import google.generativeai as genai

def digEval(image_path):

    CLIENT = InferenceHTTPClient(
        api_url="https://detect.roboflow.com",
        api_key="1sk2Fx243hvIxDG4SGIB"
    )
    results = CLIENT.infer(image_path, model_id="tata-vvrcz/4")
    # print(results)

    genai.configure(api_key="AIzaSyDo1sWjUVsVXs0XYfRoK16yvdACiq0Y8uY")
    model1 = genai.GenerativeModel(model_name="gemini-1.5-flash")
    text_height_map = {}
    sorted_text_height_map = {}
    box = 0
    result = []

    # Load your original image
    # image_path = "/content/dig.jpg"
    image = Image.open(image_path)

    # Model output in JSON format (you can replace this with actual model output if needed)
    model_output = results

    # Iterate through each detection and crop the image
    for i, prediction in enumerate(model_output['predictions']):
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
        text_height = y_center

        # Crop the image
        cropped_image = image.crop((left, top, right, bottom))

        # Convert the image to RGB mode before saving
        cropped_image = cropped_image.convert("RGB")  # Converting to RGB to remove alpha channel

        # Save the cropped image with a unique filename
        cropped_image_path = f"cropped_image_{i}.jpg"
        response = model1.generate_content(
            [cropped_image, "Extract only meaning full handwritten text in given image without any extra tags"])
        extracted_text = response.text
        print(f"Extracted Text: {extracted_text}")
        text_height_map[extracted_text] = text_height

        # Optionally display and save the results with bounding boxes and texts

        sorted_text_height_map = dict(sorted(text_height_map.items(), key=lambda item: item[1]))

        # Display the sorted map

    print("\nSorted map of extracted text by height:")
    # print(sorted_text_height_map)
    return sorted_text_height_map

# print(digEval("static/TestImages/mydig.jpg"))

