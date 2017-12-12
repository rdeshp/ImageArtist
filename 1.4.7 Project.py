import matplotlib.pyplot as plt
import os.path
import numpy as np  # "as" lets us use standard abbreviations
   
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, '1.4.5 Images\\car.jpg')
# Read the image data into an array
img = plt.imread(filename)
  
'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)



# Show the image data in a subplot
ax.imshow(img, interpolation='none')

# Show the figure on the screen
fig.show()


def blackWhiteFilter():
    height = len(img)
    width = len(img[0])
    for i in range(height):
        for j in range(width):
            val = sum(img[i][j])
            img[i][j][0] = val
            img[i][j][1] = val
            img[i][j][2] = val
    ax.imshow(img, interpolation='none')
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
    