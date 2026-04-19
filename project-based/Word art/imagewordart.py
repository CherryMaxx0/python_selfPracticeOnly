from PIL import Image
import pywhatkit

photo = Image.open("hokako/Word art/carsLMQ.png")
pywhatkit.image_to_ascii_art("\carsLMQ.png", "WordART")