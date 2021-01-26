
import os
import subprocess
import numpy as np
from pathlib import Path
from PIL import Image
# from PIL import ImageGrab

class ImageReader:

    def __init__(self):
        self.path = Path('colors/')

    def read_directory(self):
        path = self.path
        
        rgb_vals = []
        for file in path.iterdir():
            # f=open(file,'r')
            
            # Open Image
            im = Image.open(file)
            # Quantize down to 2 colour palettised image using *"Fast Octree"* method:
            q = im.quantize(colors=1)

            # Now look at the first 2 colours, each 3 RGB entries in the palette:
            rgb_val = tuple(q.getpalette()[:3])    
            rgb_vals.append(rgb_val)    
        return rgb_vals

    def create_colors(self):

        for i in range(10):
            im = Image.new(mode='RGB', size=(100, 100), color=(
                int(np.random.uniform(0,1) * 255),
                int(np.random.uniform(0,1) * 255),
                int(np.random.uniform(0,1) * 255)
                ))
            color_name = 'colors/color_{}.png'.format(str(i))
            im.save(color_name)
    
if __name__ == '__main__':
    im = ImageReader() 
    # im.create_colors()
    print(im.read_directory())