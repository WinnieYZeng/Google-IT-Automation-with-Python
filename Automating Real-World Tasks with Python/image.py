### Dwonload the file
curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=$11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" > /dev/null | curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" -o images.zip && sudo rm -rf cookie

### Install Pillow
pip3 install pillow

### Write a Python script
#!/usr/bin/env python3
import os
from PIL import Image

path = 'images'
new_path = '/opt/icons'

# iterating through images
for input_file in os.listdir(path):
    # trying to open image for formatting
    try:
        # opening image as img in RGB
        with Image.open(input_file) as img:
            img.rotate(-90).resize((128,128)).convert("RGB").save(new_path + '/' + file, format="jpeg")
            img.close()
            print(os.listdir(new_path))
    # if unable to open file
    except OSError:
        pass