import pytesseract
from PIL import Image

# Open the image using PIL
image = Image.open('MicrosoftTeams-image-2.jpg')

# Set the tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Use pytesseract to read the text from the image
text = pytesseract.image_to_string(image)

# Print the text
print(text)

