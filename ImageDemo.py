from PIL import Image

#read image
im = Image.open("duck.jpg")

#display image
# im.show()

#size of image - tuple (set of values) - width, height
print("size:", im.size)

#index 0 is width - total number of cols
# -use index 0 to refer to a specific COLUMN
print("width:", im.size[0])

#index 1 is height - total number of rows
# -use index 1 to refer to a specific ROW
print("height:", im.size[1])

pixels = im.load()
print("RGB at 0, 0:", pixels[0, 0])

#can save individual values from the tuple
r, g, b = pixels[0, 0]
print("red at 0, 0:", r)

#refer to blue value by index from the tuple
print("blue at 0, 0:", pixels[0, 0][2])

#draw a horizontal black line through the vertical middle

#find vertical middle
mid = im.size[1]/2

#iterate through each column at the middle row
for i in range(im.size[0]):
    #set pixel value to a tuple for color images
    #indexing for images is col, row
    pixels[i, mid] = (0, 0, 0)

# im.show()

#crop to keep the top half of image
#arg is a tuple representing the coordinates to keep:
#left, top, right, bottom
cropped = im.crop((0, 0, im.size[0], mid))

# cropped.show()

#crop can also add to an image to increase dimensions
cropped2 = cropped.crop((0, 0, im.size[0], mid + 100))
# cropped2.show()

#save an image to a file
cropped.save("cropped-duck.jpg")

#look for white-ish pixels and change to a different color
blueDuck = Image.new("RGB", (im.size[0], im.size[1]))
blueDuck_px = blueDuck.load()

for i in range (im.size[0]):
    for j in range (im.size[1]):
        r, g, b = pixels[i, j]
        if r > 140 and g > 140 and b > 140:
            r -= 100
            g -= 100
        blueDuck_px[i, j] = (r, g, b)

# blueDuck.show()

#split the RGB image into color channels
red, green, blue = im.split()

#each color channel is treated as b+w
# red.show()
# green.show()
# blue.show()

red_px = red.load()
#each pixel in a b+w image or indv color channel
# only has one value
print("red channel at 0, 0:", red_px[0, 0])

#merge channels into a single rgb image
merged = Image.merge("RGB", (red, green, blue))
merged.show()