
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
power = 15
x_iterator = 0 #decreases the number of pixels for the next section
y_iterator = 0
x_distance_from_center = 0
y_distance_from_center = 0 #how far away the drawn pixel is from the center
x = 80
y = 60
for y in range(y,y+power): #repeats for the power
    for i in range(power-y_iterator): #decrements for every pixel in the y axis
        for x in range(x,x+power): #repeats for the power
            for j in range(power-x_iterator): #decrements for every pixel in the x axis
                new_img.putpixel((x+x_distance_from_center,y+y_distance_from_center),original_img.getpixel((x,y)))
                x_distance_from_center +=1 #moves the drawn pixel one to the right 
            x_distance_from_center -=1 #removes the gaps
            x_iterator +=1 #decrements in the x direction
        y_distance_from_center +=1 #moves the drawn pixel one down
        x_iterator = 0 # resets the x iterator
        x_distance_from_center = 0 #resets the x distance from center
        x=80 #resets the x pos
    y_distance_from_center -=1 #removes the gap
    y_iterator +=1 #decrements in the y direction
y = 60 #resets the y pos
    

# Display student in second axes and set window to the right eye
axes[1].imshow(new_img, interpolation='none')
fig.show()
