# ============================================================         
#                                                     
# Student Name (as it appears on cuLearn): Ziwen Wang       
# Student ID (9 digits in angle brackets): <101071063>          
# Course Code (for this current semester): COMP1405A            
#                                                                   
# ============================================================       

import pygame

# Initialize pygame
pygame.init()

# Declare screen valuable 
windows = pygame.display.set_mode((48,56))

# Fill all screen to color white
windows.fill((255,255,255))

# Start draw polygon(picture)
pygame.draw.polygon(windows,(162,185,205),((23,13),(36,13),(36,19),(29,19)))

pygame.draw.polygon(windows,(55,148,201),((14,22),(14,35),(21,35),(27,29),(21,29)))

pygame.draw.polygon(windows,(124,138,80),((29,29),(36,29),(36,35),(23,35)))

pygame.draw.polygon(windows,(173,111,195),((29,37),(36,37),(36,43),(23,43)))

# Update to display screen
pygame.display.update()

# Save image 
pygame.image.save(windows,"101071063.png")





