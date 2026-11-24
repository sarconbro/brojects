

# https://academy.masterschool.com/ns/books/published/swe/ManipulatingImages/7-Exercises.html



# 7 EXERCISES


# 7.1 Fix 4 syntax errors in the code below so that it correctly sets the red in all pixels to 0.
from image import *

# CREATE AN IMAGE FROM A FILE
img = Image("gal2.jpg")

# LOOP THROUGH THE PIXELS
pixelList = img.getPixels()
for p in pixelList:

    # SET THE RED TO 0
    p.setRed(0)

    # UPDATE THE IMAGE
    img.updatePixel(p)

# SHOW THE RESULT
win = ImageWin(img.getWidth(),img.getHeight())
img.draw(win)



# 7.2 The code below makes the image have a green-blue tint. Change 1 thing in order to make it have a red tint instead.

# USE THE IMAGE LIBRARY
from image import *
# PICK THE IMAGE
img = Image("puppy.jpg")
# LOOP THROUGH THE PIXELS
pixelList = img.getPixels()
for p in pixelList:
    # SET THE COLOR
    p.setRed(255)
    # UPDATE THE PIXEL
    img.updatePixel(p)

# SHOW THE RESULT
win = ImageWin(img.getWidth(),img.getHeight())
img.draw(win)


# 7.3 Fix the indention below to correctly set the red to the green, the green to the blue, and the blue to the red.

# STEP 1: USE THE IMAGE LIBRARY
from image import *

# STEP 2: PICK THE IMAGE
img = Image("beach.jpg")

# STEP 3: LOOP THROUGH THE PIXELS
pixels = img.getPixels()
for p in pixels:

    # STEP 4: GET THE DATA
    r = p.getRed()
    g = p.getGreen()
    b = p.getBlue()

    # STEP 5: MODIFY THE COLOR
    p.setRed(g)
    p.setGreen(b)
    p.setBlue(r)

    # STEP 6: UPDATE THE IMAGE
    img.updatePixel(p)

# STEP 7: SHOW THE RESULT
win = ImageWin(img.getWidth(),img.getHeight())
img.draw(win)


# 7.4 Fix the 5 errors in the code, so that the Red pixels get the value of the green, the green get the value of blue, and the blue get the value of the red. (The cat should look purple and gray)

# STEP 1: USE THE IMAGE LIBRARY
from image import *
# STEP 2: PICK THE IMAGE
img = Image("kitten.jpg")
# STEP 3: LOOP THROUGH THE PIXELS
pixels = img.getPixels()
for p in pixels:
    # STEP 4: GET THE DATA
    r = p.getRed()
    g = p.getGreen()
    b = p.getBlue()
    # STEP 5: MODIFY THE COLOR
    p.setRed(g)
    p.setGreen(b)
    p.setBlue(r)
    # STEP 6: UPDATE THE IMAGE
    img.updatePixel(p)
# STEP 7: SHOW THE RESULT
win = ImageWin(img.getWidth(),img.getHeight())
img.draw(win)


# 7.5 Fill in the missing code on lines 9, 12, and 18 below to set the red to half the original value in all pixels in the picture.

# STEP 1: USE THE IMAGE LIBRARY
from image import *

# STEP 2: PICK THE IMAGE
img = Image("beach.jpg")

# STEP 3: LOOP THROUGH THE PIXELS
pixels = img.getPixels();
for p in pixels:

    # STEP 4: GET THE DATA
    r = p.getRed()

    # STEP 5: MODIFY THE COLOR
    p.setRed(r * 0.5)

    # STEP 6: UPDATE THE IMAGE
    img.updatePixel(p)

# STEP 7: SHOW THE RESULT
win = ImageWin(img.getWidth(),img.getHeight())
img.draw(win)


# 7.6 Complete the code in order to set the blue value to an eighth of the green value plus an eighth of the red value.

# STEP 1: USE THE IMAGE LIBRARY
from image import *
# STEP 2: PICK THE IMAGE
img = Image("swan.jpg")
# STEP 3: LOOP THROUGH THE PIXELS
pixels = img.getPixels()
for p in pixels:
    # STEP 4: GET THE DATA
    b = p.getBlue()
    g = p.getGreen()
    r = p.getRed()
    # STEP 5: MODIFY THE COLOR
    p.setBlue(((1/8) * g) + ((1/8) * r))
    
    # STEP 6: UPDATE THE IMAGE
    img.updatePixel(p)
# STEP 7: SHOW THE RESULT
win = ImageWin(img.getWidth(),img.getHeight())
img.draw(win)


# 7.7 Fix the indention in the code below so that it correctly increases the red in each pixel in the picture by 1.5.

# STEP 1: USE THE IMAGE LIBRARY
from image import *

# STEP 2: PICK THE IMAGE
img = Image("beach.jpg")

# STEP 3: LOOP THROUGH THE PIXELS
pixels = img.getPixels();
for p in pixels:

    # STEP 4: GET THE DATA
    r = p.getRed()

# STEP 5: MODIFY THE COLOR
    p.setRed(r * 1.5);

    # STEP 6: UPDATE THE IMAGE
    img.updatePixel(p)

# STEP 7: SHOW THE RESULT
win = ImageWin(img.getWidth(),img.getHeight())
img.draw(win)


# 7.8 This code is supposed to make the picture completely black; however, it is taking forever when it should only take a few seconds. Fix the code (without adding anything new) so that it runs in a few seconds.

# STEP 1: USE THE IMAGE LIBRARY
from image import *
# STEP 2: PICK THE IMAGE
img = Image("motorcycle.jpg")

# STEP 3: LOOP THROUGH THE PIXELS
pixels = img.getPixels()
for p in pixels:
    # STEP 4: GET THE DATA
    r = p.getRed()
    b = p.getBlue()
    g = p.getGreen()
    # STEP 5: MODIFY THE COLOR
    p.setRed(0)
    p.setGreen(0)
    p.setBlue(0)
    # STEP 6: UPDATE THE IMAGE
    img.updatePixel(p)
# STEP 7: SHOW THE RESULT
win = ImageWin(img.getWidth(),img.getHeight())
img.draw(win)


# 7.9 Fix the code below to correctly set the green and blue values to 0.75 times their current values.

# STEP 1: USE THE IMAGE LIBRARY
from image import *

# STEP 2: PICK THE IMAGE
img = Image("beach.jpg")

# STEP 3: LOOP THROUGH THE PIXELS
pixels = img.getPixels();
for p in pixels:
    #4: Get Data
    g = p.getGreen()
    b = p.getBlue()
    #5 : Modify
    p.setGreen(g * 0.75)
    p.setBlue(b * 0.75)
 

    # STEP 6: UPDATE THE IMAGE
    img.updatePixel(p)

# STEP 7: SHOW THE RESULT
win = ImageWin(img.getWidth(),img.getHeight())
img.draw(win)


# 7.10 The code below sets all the pixels to half their original values with one for loop. Change the code so it uses 2 for loops that utilize the range function (1 for loop should be nested in the other).

# STEP 1: USE THE IMAGE LIBRARY
from image import *
# STEP 2: PICK THE IMAGE
img = Image("baby.jpg")
# STEP 3: LOOP THROUGH THE PIXELS
for x in range(img.getWidth()):
    for y in range(img.getHeight()):
        p = img.getPixel(x, y)
        # STEP 4: GET THE DATA
        r = p.getRed()
        b = p.getBlue()
        g = p.getGreen()
        # STEP 5: MODIFY THE COLOR
        p.setRed(r//2)
        p.setGreen(g//2)
        p.setBlue(b//2)
        # STEP 6: UPDATE THE IMAGE
        img.setPixel(x, y, p)
# STEP 7: SHOW THE RESULT
win = ImageWin(img.getWidth(),img.getHeight())
img.draw(win)

# 7.11 Change the following code to set the red to 0 for all pixels in the left half of the picture.

from image import *

# CREATE AN IMAGE FROM A FILE
img = Image("gal2.jpg")

# LOOP THROUGH THE PIXELS
halfway_x = (int) (img.getWidth()/2)
for x in range(halfway_x):
    for y in range(img.getHeight()):

        # GET THE DATA
        p = img.getPixel(x, y)

        # SET THE RED TO 0
        p.setRed(0)

        # UPDATE THE IMAGE
        img.updatePixel(p)

# SHOW THE RESULT
win = ImageWin(img.getWidth(),img.getHeight())
img.draw(win)

# 7.12 The code below makes the whole image have a blue-green tint. Change the code so that it makes an only blue tint in the bottom left corner.

from image import *
# CREATE AN IMAGE FROM A FILE
img = Image("vangogh.jpg")
# LOOP THROUGH THE PIXELS
halfway_x = int(img.getWidth() // 2)
halfway_y = int(img.getHeight() // 2)
for x in range(halfway_x):
    for y in range(halfway_y, img.getHeight()):
        # GET THE DATA
        p = img.getPixel(x, y)
        # SET THE PIXEL
        p.setRed(0)
        # UPDATE THE PIXEL
        img.updatePixel(p)
# SHOW THE RESULT
win = ImageWin(img.getWidth(),img.getHeight())
img.draw(win)


# 7.13 Change the code below to set the red value in the pixels in the bottom half of the picture to 0.

from image import *

# CREATE AN IMAGE FROM A FILE
img = Image("gal2.jpg")

# LOOP THROUGH THE PIXELS
halfway_y = (int) (img.getHeight()//2)
for x in range(img.getWidth()):
    for y in range(halfway_y, img.getHeight()):

        # GET THE DATA
        p = img.getPixel(x, y)

        # SET THE RED TO 0
        p.setRed(0)

        # UPDATE THE IMAGE
        img.updatePixel(p)

# SHOW THE RESULT
win = ImageWin(img.getWidth(),img.getHeight())
img.draw(win)


# 7.14 The code below makes the whole image seem red. Change it, so that only every 5 pixels get changed, so that it will look like a red grid.

from image import *
# CREATE AN IMAGE FROM A FILE
img = Image("guy1.jpg")
# LOOP THROUGH THE PIXELS
for x in range(0, img.getWidth(), 5):
    for y in range(0,img.getHeight(), 5):
        # GET THE DATA
        p = img.getPixel(x, y)
        # SET THE PIXEL
        p.setGreen(0)
        p.setBlue(0)
        # UPDATE THE IMAGE
        img.updatePixel(p)
# SHOW THE RESULT
    win = ImageWin(img.getWidth(),img.getHeight())
    img.draw(win)


# 7.15 Change the following code into a procedure to keep only the green values in all pixels in a picture.

# STEP 1: USE THE IMAGE LIBRARY
from image import *

def keep_only_green(img):
    # STEP 3: LOOP THROUGH THE PIXELS
    pixels = img.getPixels();
    for p in pixels:
        # STEP 5: MODIFY THE COLOR
        p.setRed(0)
        p.setBlue(0)
        # STEP 6: UPDATE THE IMAGE
        img.updatePixel(p)
        
# STEP 2: PICK THE IMAGE
img = Image("beach.jpg")      
keep_only_green(img)

# STEP 7: SHOW THE RESULT
win = ImageWin(img.getWidth(),img.getHeight())
img.draw(win)


# 7.16 A grayscale picture is when the red, green, and blue value of a pixel are all equal to the average of the original pixel value. Write the code to turn the left half of an image into gray scale.

from image import *

# CREATE AN IMAGE FROM A FILE
img = Image("gal2.jpg")

# LOOP THROUGH THE PIXELS
halfway_x = (int) (img.getWidth()/2)
for x in range(halfway_x):
    for y in range(img.getHeight()):

        # GET THE DATA
        p = img.getPixel(x, y)
        r = p.getRed()
        g = p.getGreen()
        b = p.getBlue()
        grayscale = ((r+g+b)/3)

        # SET RGB EQUAL TO THE AVERAGE OF ORIGINAL VALUE
        p.setRed(grayscale)
        p.setGreen(grayscale)
        p.setBlue(grayscale)

        # UPDATE THE IMAGE
        img.updatePixel(p)

# SHOW THE RESULT
win = ImageWin(img.getWidth(),img.getHeight())
img.draw(win)


# 7.17 Define a procedure to negate an image. See Image_Negate_Quarter from Chapter 11 section 7 for how to create a negative of an image. Pass the image to the procedure. Do the import, create the image, call the prodecure, and show the result.

from image import *

# CREATE AN IMAGE FROM A FILE
img = Image("gal2.jpg")

# LOOP THROUGH THE PIXELS
for x in range(img.getWidth()):
    for y in range(img.getHeight()):

        # GET THE DATA
        p = img.getPixel(x, y)
        r = p.getRed()
        g = p.getGreen()
        b = p.getBlue()
        

        # SET RGB TO NEGATIVE
        p.setRed(255-r)
        p.setGreen(255-g)
        p.setBlue(255-b)

        # UPDATE THE IMAGE
        img.updatePixel(p)

# SHOW THE RESULT
win = ImageWin(img.getWidth(),img.getHeight())
img.draw(win)


# 7.18 Write code that takes the top half of an image and replicates it in the bottom half.

# STEP 1: USE THE IMAGE LIBRARY
from image import *

def top_half_replica(img):
    # STEP 3: LOOP THROUGH THE PIXELS
    halfway = (img.getHeight()//2)
    for x in range(img.getWidth()):
        for y in range(halfway):
            # STEP 4: GET THE DATA
            p = img.getPixel(x, y)
            # STEP 6: MODIFY THE IMAGE
            img.setPixel(x, halfway + y, p)
    
# STEP 2: PICK THE IMAGE
img = Image("../_static/vangogh.jpg")       


top_half_replica(img)    


# STEP 7: SHOW THE RESULT
win = ImageWin(img.getWidth(),img.getHeight())
img.draw(win)

# 7.19 Write a procedure to mirror an image from left to right around a vertical line in the middle of the image. Pass the image to the procedure. Do the import, create the image, call the prodecure, and show the result.

# STEP 1: USE THE IMAGE LIBRARY
from image import *

def mirror_left_to_right(img):
    # STEP 3: LOOP THROUGH THE PIXELS
    halfway = (img.getWidth()//2)
    for x in range(halfway):
        for y in range(img.getHeight()):
            # STEP 4: GET THE DATA
            p = img.getPixel(x, y)
            # STEP 6: MODIFY THE IMAGE
            img.setPixel(img.getWidth() - 1 - x, y, p)
    
# STEP 2: PICK THE IMAGE
img = Image("../_static/vangogh.jpg")       
       
# STEP 7: SHOW THE RESULT
win = ImageWin(img.getWidth(),img.getHeight())
img.draw(win)

mirror_left_to_right(img)


# 7.20 Write code that flips the image across a horizontal line.

# STEP 1: USE THE IMAGE LIBRARY
from image import *

def flip_horizontal(img):
    # STEP 3: LOOP THROUGH THE PIXELS
    halfway = (img.getHeight()//2)
    for x in range(img.getWidth()):
        for y in range(halfway):
            # STEP 4: GET THE DATA
            top_pixel = img.getPixel(x, y)
            bottom_pixel = img.getPixel(x, img.getHeight()-1-y)
            # STEP 6: MODIFY THE IMAGE
            img.setPixel(x, y, bottom_pixel)
            img.setPixel(x, img.getHeight()-1-y, top_pixel)
    
# STEP 2: PICK THE IMAGE
img = Image("../_static/vangogh.jpg")       


flip_horizontal(img)    


# STEP 7: SHOW THE RESULT
win = ImageWin(img.getWidth(),img.getHeight())
img.draw(win)











