
import PIL
import matplotlib.pyplot as plt
import os.path              


# Open the files in the same directory as the Python script
original_image = os.path.join("C:\\Users\\loren004\\Downloads\\earth.png")

# Open and show the student image in a new Figure window
new_img = PIL.Image.open(original_image)
original_img = PIL.Image.open(original_image)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(original_img, interpolation='none')

power = 5

pos = (200,200)
br_pos = (220,220)

for y in range(pos[1],br_pos[1]):
    for x in range(pos[0],br_pos[0]):
        for i in range(power):
            new_img.putpixel((2*x-210+i,y),original_img.getpixel((x,y)))


# Display student in second axes and set window to the right eye
axes[1].imshow(new_img, interpolation='none')
fig.show()


