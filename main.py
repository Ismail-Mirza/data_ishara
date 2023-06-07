from pathlib import Path
from PIL import Image
import random
import shutil


# Specify the directory path
directory_path = Path(".")

# Find all directories within the specified directory
directories = [str(path) for path in directory_path.glob("*/") if path.is_dir()]
directories.remove(".venv")
directories.remove("collected")
try:
    directories.remove("train")
    directories.remove("test")
except:
    pass
train_dir = directory_path / "train"
test_dir = directory_path / "test"
train_dir.mkdir(exist_ok=True)
test_dir.mkdir(exist_ok=True)
for directory in directories:
    dir_path = Path(directory)
    image_paths = list(dir_path.glob("*.jpg"))
    selected_image_paths = random.sample(image_paths, 47)
    # Iterate through each image path and load the image
    for image_path in image_paths[:40]:
 
        name = str(image_path).split('.')[0]
        xml_file = name + '.xml'
        shutil.move(str(image_path), train_dir)
        shutil.move(xml_file, train_dir)
    for image_path in image_paths[41:]:
        name = str(image_path).split('.')[0]
        xml_file = name + '.xml'
        shutil.move(str(image_path), test_dir)
        shutil.move(xml_file, test_dir)

   


# Move the selected images to the train directory
# for image_path in selected_images[:num_train]:
#     shutil.move(image_path, train_dir)

# # Move the remaining selected images to the test directory
# for image_path in selected_images[num_train:]:
#     shutil.move(image_path, test_dir)
print(train_images)
    

# Now you have a list of all directories within the specified directory



# Now you have a list containing all the loaded images
