# ============================================================
#
# Student Name (as it appears on cuLearn): Ziwen Wang
# Student ID (9 digits in angle brackets): <101071063>
# Course Code (for this current semester): COMP1405A
#
# ============================================================

import pygame

# Ask user some questions to finish program
instruction = input("Would you like to get some instructions of this program? (yes/no) " )

if instruction.lower() == "yes" :
    print("* You will be asked some questions \n* The question will ask you the filename of background and ghost, you need to enter a valid filename to make sure the program can continue \n* The question also will ask you the x_axis and y_axis of the ghost place where it is display \n* Please make sure you give the valid integer number to continue program")

background_image_filename = input("\nPlease enter the filename of the background image! ")

# initialize and declare variables

pygame.init()

windows = pygame.display.set_mode((0,0))

background_image = pygame.image.load(background_image_filename)

(background_width,background_height) = background_image.get_rect().size

windows = pygame.display.set_mode((background_width,background_height))

windows.blit(background_image,(0,0))

pygame.display.update()

ghost_image_filename = input("\nPlease enter the filename of the ghost image! " )

ghost_image = pygame.image.load(ghost_image_filename)

(ghost_width,ghost_height) = ghost_image.get_rect().size

user_x_axis = int(input("\nwhat is the x_axis of ghost that you want to display for? "))

# Using loop to ask user again if the number that user input is out of range
while (user_x_axis > background_width or user_x_axis < 0 ):
    print("\nSoryy! Please enter again, your number is out of range.")
    user_x_axis = int(input("\nwhat is the x_axis of ghost that you want to display for? "))
    
user_y_axis = int(input("\nwhat is the y_axis of ghost that you want to display for? "))

# Using loop to ask user again if the number that user input is out of range
while (user_y_axis > background_height or user_y_axis < 0 ):
    print("\nSoryy! Please enter again, your number is out of range.")
    user_y_axis = int(input("\nwhat is the y_axis of ghost that you want to display for? "))

# Using nested loop to get every pixel color 
for i in range(ghost_width):
    for j in range(ghost_height):
        (red1,green1,blue1,other1) = ghost_image.get_at((i,j))
        if user_x_axis + i -int(ghost_width/2) <= background_width and user_y_axis + j - int(ghost_height) <= background_height and user_x_axis + i - int(ghost_width/2) >= 0 and user_y_axis + j -int(ghost_height/2) >=0:
            (red2,green2,blue2,other2) = background_image.get_at((user_x_axis + i - int(ghost_width/2),user_y_axis + j - int(ghost_height/2)))
            if (red1,green1,blue1) != (0,255,0):# if the pixel not green, set the pixel from ghost to background and set average color
                background_image.set_at((user_x_axis + i - int(ghost_width/2),user_y_axis + j - int(ghost_height/2)),(((red1 + red2)/2),((green1 + green2)/2), ((blue1 + blue2)/2)))
            
                
clicked = False
myfont = pygame.font.SysFont('Sans', 25)

while True:

    # QUIT event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit() # Close pygame window
            pygame.quit()
            exit()
        # Click and move the image
        if event.type == pygame.MOUSEMOTION:
            if (clicked==True):
                user_x_axis,user_y_axis=pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
                x,y=pygame.mouse.get_pos()
                if (x > user_x_axis-50 and x < user_x_axis+50 and y > user_y_axis-50 and y < user_y_axis+50):
                    clicked = not clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = not clicked
            
    # Display the image in the screen
    #windows.blit(ghost_image,(user_x_axis-ghost_width/2,user_y_axis-ghost_height/2))
    windows.blit(background_image,(0,0))
    if (clicked==True):
        x,y=pygame.mouse.get_pos()
        textsurface = myfont.render("("+str(x)+", "+str(y)+")", True, (255, 0, 0))
        windows.blit(textsurface,(x-50, y))
    
    pygame.display.update()



    
    
    
    
