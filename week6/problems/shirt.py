import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) != 3:
    sys.exit("Must be exactly two filenames")

input = sys.argv[1]
output = sys.argv[2]

valid_inputs = (".jpg", ".jpeg", ".png")

   
if not input.lower().endswith(valid_inputs) or not output.lower().endswith(valid_inputs):
    sys.exit("Both must be jpg, jpeg, or png files")

int_ext = os.path.splitext(input)[1].lower()
out_ext = os.path.splitext(output)[1].lower()

if int_ext != out_ext:
    sys.exit("Both files must be the same file type")

try:
    photo = Image.open(input)
    shirt = Image.open("shirt.png")

    photo = ImageOps.fit(photo, shirt.size)
    
    photo.paste(shirt, shirt)

    photo.save(output)
    

except(FileNotFoundError):
    sys.exit("Could not find file")