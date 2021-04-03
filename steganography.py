from PIL import Image, ImageDraw 
from random import randint


class Steganography:
    def __init__(self):
        pass

    def Encrypt(self, input_text_path, input_image_path, output_image_path):	   
        image = Image.open(input_image_path)
        draw = ImageDraw.Draw(image)
        pix = image.load()

        text = open(input_text_path, 'r')

        def index():
            width = image.size[0]
            height = image.size[1]	
            for i in range(width):
                for j in range(height):
                    yield (i, j)
        indexes = index()
        for line in text:
            for number in ([ord(char) for char in line]):
                 xy = next(indexes)
                 g, b = pix[xy][1:3]
                 draw.point(xy, (number, g , b))							

        image.save(output_image_path, "PNG")
        text.close()

    def Decrypt(self, input_image_path, output_text_path):
        numbers = []
        image = Image.open(input_image_path)				
        pixels = image.load()

        def index():
            width = image.size[0]
            height = image.size[1]	
            for i in range(width):
                for j in range(height):
                    yield (i, j)
        indexes = index()
        
        for i in range(1000):
            numbers.append(pixels[tuple(next(indexes))][0])

        output_text = open(output_text_path, 'a')
        output_text = open(output_text_path, 'w')
        output_text.write(''.join([chr(number) for number in numbers]))
        output_text.close()

steganography_en = Steganography()											
steganography_en.Encrypt("steganography/input.txt", "steganography/image.png", "steganography/image2.png")
steganography_de = Steganography()											
steganography_de.Decrypt("steganography/image2.png", "steganography/output.txt")
