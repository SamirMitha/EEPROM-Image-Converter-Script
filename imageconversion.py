from PIL import Image

image = Image.open("IMAGENAME.png")
layout = image.load()

out_file = open("IMAGENAME.bin", "wb")

for j in range(256):
    for i in range(128):
        try:
            out_file.write(chr(layout[i,j]))
        except IndexError:
            out_file.write(chr(0))