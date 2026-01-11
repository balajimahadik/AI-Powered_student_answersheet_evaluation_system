from ultralytics import YOLO
import cv2
from PIL import Image
import google.generativeai as genai
import time
import os
from dotenv import load_dotenv
# Import the cv2_imshow function from google.colab.patches

# text_height_map = {}
#

#
# # Load the YOLO model
# model = YOLO("O:\\IPCV\\CP\\FinalCP\\Models\\best.pt")  # pretrained YOLO model
#
# # Run inference on an image
# results = model("O:\\IPCV\\CP\\FinalCP\\static\\TestImages\\diagram1.jpg")
#
#
# # Load the original image (needed for cropping)
# original_image = cv2.imread("O:\\IPCV\\CP\\FinalCP\\static\\TestImages\\diagram1.jpg")
#
# model1 = genai.GenerativeModel(model_name="gemini-1.5-flash")
#
# print(results)
# print("\n")
#
# # Assuming 'results' is a list of result objects from YOLO inference
# for result in results:
#     # Accessing the original image from result
#     original_image = result.orig_img  # Image in numpy array format
#
#     # Access the boxes object from the result
#     boxes = result.boxes  # Boxes object for bounding box outputs
#
#     # Loop through each box (detection)
#     for i, box in enumerate(boxes):
#         # Check if the class ID matches the 'text' class (which has class_id 4)
#         class_id = int(box.cls[0])  # Class ID for the current detection
#
#         if class_id == 4:  # Class ID for 'text'
#             print("Detected text block")
#
#             # Extract bounding box coordinates
#             x1, y1, x2, y2 = map(int, box.xyxy[0])  # Box coordinates in [x1, y1, x2, y2] format
#             text_height = y2
#
#             # Crop the detected region (text) from the original image
#             cropped_region = original_image[y1:y2, x1:x2]
#             cropped_pil_image = Image.fromarray(cropped_region)
#
#             time.sleep(2)
#             response = model1.generate_content([cropped_pil_image, "Extract only meaning full handwritten text in given image without any extra tags"])
#             extracted_text =response.text
#             print(f"Extracted Text: {extracted_text}")
#             box.text = extracted_text
#             text_height_map[extracted_text] = text_height
#
#
#
#     # Optionally display and save the results with bounding boxes and texts
#     result.show()  # Display the image with detections
#     result.save(filename="result_with_text.jpg")
#
#     sorted_text_height_map = dict(sorted(text_height_map.items(), key=lambda item: item[1]))
#
# # Display the sorted map
#     print("\nSorted map of extracted text by height:")
#     print(sorted_text_height_map)


def blockDigEval(image_Path):
    text_height_map = {}
    load_dotenv()

    api_key = os.getenv('API_KEY')
    genai.configure(api_key=api_key)

    # Load the YOLO model
    model = YOLO("O:\\IPCV\\CP\\FinalCP\\Models\\best.pt")  # pretrained YOLO model

    # Run inference on an image
    results = model(image_Path)

    # Load the original image (needed for cropping)
    original_image = cv2.imread(image_Path)

    model1 = genai.GenerativeModel(model_name="gemini-1.5-flash")

    print(results)
    print("\n")

    # Assuming 'results' is a list of result objects from YOLO inference
    for result in results:
        # Accessing the original image from result
        original_image = result.orig_img  # Image in numpy array format

        # Access the boxes object from the result
        boxes = result.boxes  # Boxes object for bounding box outputs

        # Loop through each box (detection)
        for i, box in enumerate(boxes):
            # Check if the class ID matches the 'text' class (which has class_id 4)
            class_id = int(box.cls[0])  # Class ID for the current detection

            if class_id == 4:  # Class ID for 'text'
                print("Detected text block")

                # Extract bounding box coordinates
                x1, y1, x2, y2 = map(int, box.xyxy[0])  # Box coordinates in [x1, y1, x2, y2] format
                text_height = y2

                # Crop the detected region (text) from the original image
                cropped_region = original_image[y1:y2, x1:x2]
                cropped_pil_image = Image.fromarray(cropped_region)

                time.sleep(2)
                response = model1.generate_content([cropped_pil_image,
                                                    "Extract only meaning full handwritten text in given image without any extra tags"])
                extracted_text = response.text
                print(f"Extracted Text: {extracted_text}")
                box.text = extracted_text
                text_height_map[extracted_text] = text_height

        # Optionally display and save the results with bounding boxes and texts
        result.show()  # Display the image with detections
        result.save(filename="result_with_text.jpg")

        sorted_text_height_map = dict(sorted(text_height_map.items(), key=lambda item: item[1]))

        # Display the sorted map
        print("\nSorted map of extracted text by height:")
        print(sorted_text_height_map)

    return sorted_text_height_map
