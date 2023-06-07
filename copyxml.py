from pathlib import Path
import os

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
xml_dictionary = {}
for directory in directories:
    dir_path = Path(directory)
    image_paths = list(dir_path.glob("*.xml"))
    for image_path in image_paths:
        [sub_dir,name] = str(image_path).split('\\')
        xml_dictionary[name] = sub_dir
        

input_path = Path("train")
image_paths = input_path.glob("*.jpg")
import shutil


for image_path in image_paths:
    [sub_dir,name] = str(image_path).split('\\')
    name = name.split('.')[0]
    xml_name  = name + '.xml'
    sub_dir=xml_dictionary.get(xml_name)
    if sub_dir:
        new_path = os.path.join(sub_dir,xml_name)
        shutil.move(new_path,input_path)






