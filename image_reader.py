
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
        
        for file in path.iterdir():
            f=open(file,'r')
    
    def create_colors(self):
        path = self.path 

        for i in range(10):
            Image.new(mode='RGB', color)
        # subprocess.call(['cd', 'colors/'], shell=True)
        # subprocess.call('ls', shell=True)
    
if __name__ == '__main__':
    im = ImageReader() 
    im.create_colors()