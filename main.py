
# fontpath = "ttf/NRT-Reg.ttf"
#
# text = " بۆ حەمە کرماشان!"


import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np

font_path = 'ttf/NRT-Reg.ttf'
font_size = 24  # Adjust the font size as needed
font = ImageFont.truetype(font_path, font_size)

capture = cv2.VideoCapture(0)  # Replace 0 with the appropriate camera index if multiple cameras are connected

while True:
    # Capture frame from camera
    ret, frame = capture.read()

    # Convert frame to PIL Image
    pil_image = Image.fromarray(frame)

    # Create a PIL ImageDraw object to draw text
    draw = ImageDraw.Draw(pil_image)

    # Define the text message
    text = "بۆ حەمە کرماشان"

    # Get the bounding box of the text
    text_bbox = draw.textbbox((0, 0), text, font=font)

    # Extract the width and height from the bounding box
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # Calculate the position to display the text
    x = int((frame.shape[1] - text_width) / 2)  # Centers the text horizontally
    y = int((frame.shape[0] - text_height) / 2)  # Centers the text vertically

    # Draw the text on the PIL image
    draw.text((x, y), text, font=font, fill=(255, 255, 255))

    # Convert the PIL image back to a NumPy array
    output_frame = np.array(pil_image)

    # Show the frame
    cv2.imshow('Custom Font', output_frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the resources and close the windows
capture.release()
cv2.destroyAllWindows()
