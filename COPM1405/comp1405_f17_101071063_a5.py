# ============================================================
#
# Student Name (as it appears on cuLearn): Ziwen Wang
# Student ID (9 digits in angle brackets): <101071063>
# Course Code (for this current semester): COMP1405A
#
# ============================================================

from comp1405_f17_assistant_a5 import *


# First leg use for loop
for i in range(9):
	move_down() 

# Second leg use for loop
for j in range(40):
	move_right()

# Thrid leg use precondition while loop  
while what_number_am_i_standing_on() != 5:
	move_down()

# Fourth leg use postcondition while loop with break statement
while True:
	move_left()
	if am_i_standing_on(1):
		break

# Fifth leg use postcondition while loop with Boolean flag
boolFlag = True
while boolFlag:
	move_down()

	if am_i_standing_on(5):
		boolFlag = False

# Sixth leg use perconsidtion while loop
while am_i_standing_on(1) == False:
	move_right()

# Seventh leg use postcondition while loop with break statement 
while True:
	move_down()
	if what_number_am_i_standing_on() == 5:
		break

# Eighth leg use postcondition while loop with Boolean flag
boolFlag = True
while boolFlag:
	move_left()
	if what_number_am_i_standing_on() == 1:
		boolFlag = False

# Ninth leg use for loop 
for t in range(7):
	move_down()

	

	

	

	
	

