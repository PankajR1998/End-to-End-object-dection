import os
import cv2
import time
import uuid

IMAGE_DIR = "CollectImages"
labels = ['Hello','Yes','No','ILoveYou','Please']

number_of_images = 5

for label in labels:
    img_path = os.path.join(IMAGE_DIR,label)
    os.makedirs(img_path)

    # open camera
    cap = cv2.VideoCapture(0)
    print(f"Collecting image for {label}")
    time.sleep(4)

    for imgnum in range(number_of_images):
        return_status, frame = cap.read()
        image_name = os.path.join(img_path,f"{label}.{uuid.uuid1()}.jpg")
        cv2.imwrite(image_name,frame)
        cv2.imshow("frame",frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF==ord('q'):
            break

    cap.release()


