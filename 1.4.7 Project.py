import matplotlib.pyplot as plt
import os.path
import numpy as np  # "as" lets us use standard abbreviations
import PIL
   
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, '1.4.5 Images\\car.jpg')
# Read the image data into an array
img = PIL.Image.open(filename)
  
'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)



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
    
    
def frame(thickness = 10):
    height = len(img)
    width = len(img[0])    
    
    image_sheet = Image.new("RGBA", (max_width * len(images), max_height))
    
    
    
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
    