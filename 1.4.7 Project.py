import matplotlib.pyplot as plt
import os.path
import numpy as np  # "as" lets us use standard abbreviations
import PIL
from matplotlib.widgets import Slider, Button, RadioButtons
   
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, '1.4.5 Images\\flower2.jpg')
# Read the image data into an array
img = PIL.Image.open(filename)

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)



# Show the image data in a subplot
ax.imshow(img, interpolation='none')

# Show the figure on the screen
fig.show()

def loadImg(imgName):
    directory = os.path.dirname(os.path.abspath(__file__)) 
    # Build an absolute filename from directory + filename
    filename = os.path.join(directory, '1.4.5 Images\\'+imgName+'.jpg')
    # Read the image data into an array
    img = PIL.Image.open(filename)
        
    
    # Show the image data in a subplot
    ax.imshow(img, interpolation='none')
    
    # Show the figure on the screen
    fig.show()

def blackWhiteFilter():
    width, height = img.size
    pixels = img.load()
    for i in range(height):
        for j in range(width):
            r, g, b = img.getpixel((j, i))
            val = (r + g + b)/3
            if img.mode == 'RGB':
                shade = (val, val, val)
            elif img.mode == 'RGBA':
                shade = (val, val, val, 255)
            pixels[j,i]= shade
    ax.imshow(img, interpolation='none')
    # Show the figure on the screen
    fig.show()
    
def blackWhiteGeo():
    width, height = img.size
    pixels = img.load()
    for i in range(height):
        for j in range(width):
            r, g, b = img.getpixel((j, i))
            val = int((r*g*b)**(1/3.0))
            if img.mode == 'RGB':
                shade = (val, val, val)
            elif img.mode == 'RGBA':
                shade = (val, val, val, 255)
            pixels[j,i]= shade
    ax.imshow(img, interpolation='none')
    # Show the figure on the screen
    fig.show()
    

def keyFilter(red, green, blue, thresh):
    width, height = img.size
    pixels = img.load()
    for i in range(height):
        for j in range(width):
            r, g, b = img.getpixel((j, i))
            difference = (red-r)**2 + (green-g)**2+ (blue-b)**2
            
            if difference > thresh and img.mode == 'RGB':
                val = int((r*g*b)**(1/3.0))
                if img.mode == 'RGB':
                    shade = (val, val, val)
                elif img.mode == 'RGBA':
                    shade = (val, val, val, 255)
                pixels[j,i]= shade
    ax.imshow(img, interpolation='none')
    # Show the figure on the screen
    fig.show()


def addColor(red, green, blue):
    width, height = img.size
    pixels = img.load()
    for i in range(height):
        for j in range(width):
            r, g, b = img.getpixel((j, i))
            newRed = r + red
            newGreen = g + green
            newBlue = b + blue
            
            if newRed > 255:
                newRed = 255
            if newGreen > 255:
                newGreen = 255
            if newBlue > 255:
                newBlue = 255
            if img.mode == 'RGB':
                shade = (newRed, newGreen, newBlue)
            elif img.mode == 'RGBA':
                shade = (newRed, newGreen, newBlue, 255)
            pixels[j,i]= shade
    ax.imshow(img, interpolation='none')
    # Show the figure on the screen
    fig.show()



def frame(thickness = 20, color = (0,0,0)):
    width, height = img.size  
    image_sheet = PIL.Image.new("RGB", (width+2*thickness, height+2*thickness), color)
    newPixels = image_sheet.load()
    for i in range(height):
        for j in range(width):
            r, g, b = img.getpixel((j, i))
            shade = (r, g, b)
            newPixels[j+thickness,i+thickness]= shade
    ax.imshow(image_sheet, interpolation='none')
    # Show the figure on the screen
    fig.show()
    
    
    
def reloadImage():
    directory = os.path.dirname(os.path.abspath(__file__)) 
    # Build an absolute filename from directory + filename
    filename = os.path.join(directory, '1.4.5 Images\\car.jpg')
    # Read the image data into an array
    img = plt.imread(filename)
        
    
    # Show the image data in a subplot
    ax.imshow(img, interpolation='none')
    
    # Show the figure on the screen
    fig.show()
    
def saveImg(imgName):
    directory = os.path.dirname(os.path.abspath(__file__)) 
    # Build an absolute filename from directory + filename
    filename = os.path.join(directory, 'Output Images\\'+imgName+'.png')
    img.save(filename, "PNG")
    