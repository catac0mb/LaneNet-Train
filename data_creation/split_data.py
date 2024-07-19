import os
from sklearn.model_selection import train_test_split

filenames = os.listdir('C:/LaneNet-Train/data/image/Left_filenames')

X_train, X_test = train_test_split(filenames, test_size=0.2)

train_file = open('C:/LaneNet-Train/data/image/left_train.txt', 'a')
for filename in X_train:
    train_file.write('C:/LaneNet-Train/data/image/Left_test_files/Left_resized_512x256/{} C:/LaneNet-Train/data/image/Left_test_files/Left_512x256_binary_medianblur/{} C:/LaneNet-Train/data/image/Left_test_files/Left_512x256_instance/{} \n'
                     .format(filename, filename, filename))
    
train_file.close()

test_file = open('C:/LaneNet-Train/data/image/left_test.txt', 'a')
for filename in X_test:
    test_file.write('C:/LaneNet-Train/data/image/Left_test_files/Left_resized_512x256/{} C:/LaneNet-Train/data/image/Left_test_files/Left_512x256_binary_medianblur/{} C:/LaneNet-Train/data/image/Left_test_files/Left_512x256_instance/{} \n'
                     .format(filename, filename, filename))
    
test_file.close()

