import gradio as gr
from PIL import Image
import numpy as np
from ultralytics import YOLO
from paddleocr import PaddleOCR

# Load the license plate segmentation model (YOLOv8)
segmentation_model = YOLO('plate_segment_best.pt')

# Function to process the image and extract plate number
def process_image(image):
    # Convert PIL image to numpy array
    image_np = np.array(image)

    # Perform license plate segmentation using the YOLOv8 model
    results = segmentation_model(image_np)

    # Extract the bounding box with the highest confidence score
    boxes = results[0].boxes.xyxy.numpy()
    if len(boxes) == 0:
        return None

    # Assuming the first box is the license plate (you can adjust based on your model's output)
    x1, y1, x2, y2 = boxes[0]
    segmented_plate = image_np[int(y1):int(y2), int(x1):int(x2)]

    # Use PaddleOCR to extract text from the segmented plate area
    ocr = PaddleOCR(use_angle_cls=True, lang='en')
    ocr_results = ocr.ocr(segmented_plate, cls=True)

    # Extract the plate number from OCR results
    plate_number = extract_plate_number(ocr_results)

    return plate_number

# Function to extract plate number from OCR results
def extract_plate_number(ocr_results):
    plate_number = ""
    for line in ocr_results:
        for word in line:
            plate_number += word[1][0] + " "
    return plate_number.strip()

def detect_plate(image, suspected_numbers):
    suspected_plates = [num.strip() for num in suspected_numbers.split('\n') if num.strip()]
    
    plate_number = process_image(image)
    if plate_number:
        if plate_number in suspected_plates:
            return f'Detected License Plate Number: {plate_number}\n**Wanted Car Detected!**'
        else:
            return f'Detected License Plate Number: {plate_number}\nCar is not in the Wanted list.'
    else:
        return 'License Plate Number could not be extracted.'

# Gradio interface
def main():
    suspected_numbers_input = gr.Textbox(lines=5, label="Enter wanted plate numbers (one per line)")
    image_input = gr.Image(type="pil", label="Upload an image")
    output_text = gr.Textbox(label="Detection Result")
    
    gr.Interface(fn=detect_plate, inputs=[image_input, suspected_numbers_input], outputs=output_text, live=True).launch(share=True)

if __name__ == '__main__':
    main()