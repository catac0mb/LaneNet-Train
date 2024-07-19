import cv2
import os
import shutil

read_path = 'C:/LaneNet-Train/data/Additional_images/Right_instance'
write_path = 'C:/LaneNet-Train/data/Additional_images/Right_binary'

if os.path.exists(write_path):
    shutil.rmtree(write_path)
os.mkdir(write_path)


print("Processing images...")
for file in os.listdir(read_path):
    # Read the image in grayscale
    image = cv2.imread(os.path.join(read_path, file), cv2.IMREAD_GRAYSCALE)

    # Apply Median blur
    blurred_image = cv2.medianBlur(image, 5)

    # Apply binary threshold
    _, binary_image = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    #_, binary_image = cv2.threshold(cv2.imread(os.path.join(read_path, file), cv2.IMREAD_GRAYSCALE), 0, 255, cv2.THRESH_BINARY)
    
    cv2.imwrite(os.path.join(write_path, file), binary_image)
                
print("Done!")