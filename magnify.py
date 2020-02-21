
import PIL
import matplotlib.pyplot as plt
import os.path              
#x and y are the coordinates of the pixel being copied
#x_pos and y_pos are the coordinates of the magnify
def stretch(x_pos,y_pos,power,original_image):
    try:
        new_img = PIL.Image.open(original_image)
        original_img = PIL.Image.open(original_image)
    except SyntaxError, IOError: #If there is an error then stop the program and tell them they messed up
        print("failed to open image, please supply a proper path")
    fig, axes = plt.subplots(1, 2)
    axes[0].imshow(original_img, interpolation='none')
    x_iterator = 0 #decreases the number of pixels for the next section
    y_iterator = 0
    x_distance_from_center = 0
    y_distance_from_center = 0 #how far away the drawn pixel is from the center
    x = x_pos
    y = y_pos
    #top left
    for y in range(y,y+power): #repeats for the power
        for i in range(power-y_iterator): #decrements for every pixel in the y axis
            for x in range(x,x+power): #repeats for the power
                for j in range(power-x_iterator): #decrements for every pixel in the x axis
                    try:
                        new_img.putpixel((x-x_distance_from_center,y+y_distance_from_center),original_img.getpixel((x,y)))
                    except IndexError:
                        pass # if there is an error then ignore the error 
                    x_distance_from_center +=1 #moves the drawn pixel one to the right 
                x_distance_from_center -=1 #removes the gaps
                x_iterator +=1 #decrements in the x direction
            y_distance_from_center +=1 #moves the drawn pixel one down
            x_iterator = 0 # resets the x iterator
            x_distance_from_center = 0 #resets the x distance from center
            x=x_pos #resets the x pos
        y_distance_from_center -=1 #removes the gap
        y_iterator +=1 #decrements in the y direction
        x_iterator = 0 #decreases the number of pixels for the next section
    y_iterator = 0
    x_distance_from_center = 0
    y_distance_from_center = 0 #how far away the drawn pixel is from the center
    x = x_pos
    y = y_pos
    #top right
    for y in range(y,y+power): #repeats for the power
        for i in range(power-y_iterator): #decrements for every pixel in the y axis
            for x in range(x,x+power): #repeats for the power
                for j in range(power-x_iterator): #decrements for every pixel in the x axis
                    try:
                        new_img.putpixel((x+x_distance_from_center,y-y_distance_from_center),original_img.getpixel((x,y)))
                    except IndexError:
                        pass # if there is an error then ignore the error 
                    x_distance_from_center +=1 #moves the drawn pixel one to the right 
                x_distance_from_center -=1 #removes the gaps
                x_iterator +=1 #decrements in the x direction
            y_distance_from_center +=1 #moves the drawn pixel one down
            x_iterator = 0 # resets the x iterator
            x_distance_from_center = 0 #resets the x distance from center
            x=x_pos #resets the x pos
        y_distance_from_center -=1 #removes the gap
        y_iterator +=1 #decrements in the y direction
        x_iterator = 0 #decreases the number of pixels for the next section
    y_iterator = 0
    x_distance_from_center = 0
    y_distance_from_center = 0 #how far away the drawn pixel is from the center
    x = x_pos
    y = y_pos
    #bottom left
    for y in range(y,y+power): #repeats for the power
        for i in range(power-y_iterator): #decrements for every pixel in the y axis
            for x in range(x,x+power): #repeats for the power
                for j in range(power-x_iterator): #decrements for every pixel in the x axis
                    try:
                        new_img.putpixel((x-x_distance_from_center,y-y_distance_from_center),original_img.getpixel((x,y)))
                    except IndexError:
                        pass # if there is an error then ignore the error 
                    x_distance_from_center +=1 #moves the drawn pixel one to the right 
                x_distance_from_center -=1 #removes the gaps
                x_iterator +=1 #decrements in the x direction
            y_distance_from_center +=1 #moves the drawn pixel one down
            x_iterator = 0 # resets the x iterator
            x_distance_from_center = 0 #resets the x distance from center
            x=x_pos #resets the x pos
        y_distance_from_center -=1 #removes the gap
        y_iterator +=1 #decrements in the y direction
        x_iterator = 0 #decreases the number of pixels for the next section
    y_iterator = 0
    x_distance_from_center = 0
    y_distance_from_center = 0 #how far away the drawn pixel is from the center
    x = x_pos
    y = y_pos
    #bottom right
    for y in range(y,y+power): #repeats for the power
        for i in range(power-y_iterator): #decrements for every pixel in the y axis
            for x in range(x,x+power): #repeats for the power
                for j in range(power-x_iterator): #decrements for every pixel in the x axis
                    try:
                        new_img.putpixel((x+x_distance_from_center,y+y_distance_from_center),original_img.getpixel((x,y)))
                    except IndexError:
                        pass # if there is an error then ignore the error 
                    x_distance_from_center +=1 #moves the drawn pixel one to the right 
                x_distance_from_center -=1 #removes the gaps
                x_iterator +=1 #decrements in the x direction
            y_distance_from_center +=1 #moves the drawn pixel one down
            x_iterator = 0 # resets the x iterator
            x_distance_from_center = 0 #resets the x distance from center
            x=x_pos #resets the x pos
        y_distance_from_center -=1 #removes the gap
        y_iterator +=1 #decrements in the y direction
        x_iterator = 0 #decreases the number of pixels for the next section
    y_iterator = 0
    x_distance_from_center = 0
    y_distance_from_center = 0 #how far away the drawn pixel is from the center
    x = x_pos
    y = y_pos
    axes[1].imshow(new_img, interpolation='none')
    fig.show()