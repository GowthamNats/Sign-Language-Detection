# Necessary Imports
import os
import cv2
import time
import uuid

# Necessary Constants
IMAGE_PATH = 'CollectedImages'
labels = ['Hello', 'Yes', 'No', 'Thanks', 'IloveYou', 'Please']
number_of_images = 20

# Iterating through the labels to:
for label in labels:

    # Create label-specific directories
    img_path = os.path.join(IMAGE_PATH, label)
    os.makedirs(img_path)

    # Capture images
    cap = cv2.VideoCapture(0)
    print('Collecting images for {}'.format(label))
    time.sleep(5)

    # Loop through the captured images to
    for imgnum in range(number_of_images):

        # Capture a single frame
        ret, frame = cap.read()

        # Store in this particular file format
        imagename = os.path.join(IMAGE_PATH, label, label + '.' + '{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imagename, frame)

        # View the frame
        cv2.imshow('frame', frame)
        time.sleep(2)
        
        # Exit the loops
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release the webcam
    cap.release()