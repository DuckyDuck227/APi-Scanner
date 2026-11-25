# Secret is hidden inside the pixel data of an image file (steganography).
# The image looks completely normal to the eye and to any text scanner -
# the key only comes out if you know the exact extraction algorithm.
from PIL import Image
img = Image.open("logo.png")
api_key = extract_hidden_bits(img)  # custom steganography decoder, not shown
