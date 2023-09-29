import os
import yaml
from PIL import Image, ImageOps

print('generating...')

with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

palette =config['palette']

for source in os.listdir("img"):
    img = Image.open("img/"+ source)
    img = ImageOps.grayscale(img)
    img = img.resize((config['res_x'], config['res_y']))
    art = ""
    for y in range(img.height):
        for x in range(img.width):
            #get pixel value between 0 and 1
            pixel = img.getpixel((x,y))/255
            #locate palette character
            art += palette[int(round(pixel * len(palette)-1))]
            
        art += "\n"

    with open('output/'+source+'.txt', 'w') as f:
        f.write(art)

print('done!')
