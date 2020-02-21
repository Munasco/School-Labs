import numpy as np
from PIL import Image

#take path to an image file ('.png' file) as input and return 
#a list representation of the image
def image_to_list(filename):
	img = Image.open(filename)
	img.load()
	data = np.asarray(img, dtype="int32")
	return data.tolist()

#take list representation of an image and save it as a '.png' file named filename
def write_image(image_list, filename):
	if '.png' not in filename:
		print("ERROR: Image should be saved in .png format")
		return -1
	image = np.array(image_list, dtype=np.uint8)
	im = Image.fromarray(image)
	im.save(filename)

        
