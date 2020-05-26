#!/usr/bin/env python3

import os, glob
from PIL import Image

size = 128, 128
old_path = 'OLD_PATH_HERE'
path = 'NEW_PATH_HERE'
rotation = 270
format = 'JPEG'

for file in glob.glob(os.getcwd() + old_path):

  img = Image.open(file).convert('RGB')
  new_name = os.path.basename(file)
  im.rotate(rotation).resize((size)).save(path + new_name, format)
