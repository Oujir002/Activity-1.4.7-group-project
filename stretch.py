
import PIL
import matplotlib.pyplot as plt
import os.path              


# Open the files in the same directory as the Python script
original_image = os.path.join("C:\\Users\\loren004\\Downloads\\earth.png")

# Open and show the student image in a new Figure window
middle_img = PIL.Image.open(original_image)
new_img = PIL.Image.open(original_image)
original_img = PIL.Image.open(original_image)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(original_img, interpolation='none')

power = 3

pos = (200,200)
br_pos = (220,220)
#top right
x_mid = (pos[0]+br_pos[0])/2
y_mid = (pos[1]+br_pos[1])/2
for y in range(pos[1]-1,y_mid+1):
    for x in range(x_mid-1,br_pos[0]+1):
        for ix in range(power):
            for iy in range(power):
                new_img.putpixel((x+(x-x_mid)*(power-1)+ix,y-(y_mid-y)*(power-1)-iy),original_img.getpixel((x,y)))
#bottom right
for y in range(y_mid-1,(br_pos[1])+1):
    for x in range(x_mid-1,br_pos[0]+1):
        for ix in range(power):
            for iy in range(power):
                new_img.putpixel((x+(x-x_mid)*(power-1)+ix,y+(y-y_mid)*(power-1)+iy),original_img.getpixel((x,y)))
#bottom left
for y in range(y_mid-1,(br_pos[1])+1):
    for x in range(pos[0]-1,x_mid+1):
        for ix in range(power):
            for iy in range(power):
                new_img.putpixel((x-(x_mid-x)*(power-1)-ix,y+(y-y_mid)*(power-1)+iy),original_img.getpixel((x,y)))
#top left
for y in range(pos[1]-1,y_mid+1):
    for x in range(pos[0]-1,x_mid+1):
        for ix in range(power):
            for iy in range(power):
                new_img.putpixel((x-(x_mid-x)*(power-1)-ix,y-(y_mid-y)*(power-1)-iy),original_img.getpixel((x,y)))



# Display student in second axes and set window to the right eye
axes[1].imshow(new_img, interpolation='none')
fig.show()


