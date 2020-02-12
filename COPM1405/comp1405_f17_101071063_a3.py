# ============================================================
#
# Student Name (as it appears on cuLearn): ziwen wang
# Student ID (9 digits in angle brackets): <101071063>
# Course Code (for this current semester): COMP1405A
#
# ============================================================

from comp1405_f17_assistant_a3 import *

def decision_making_function(e):  # 'e' IS THE SHAPE ARGUMENT YOU MUST PASS TO YOUR PERMITTED FUNCTIONS

	condition_for_sending_down =  color_is_blue(e) and wrapped_in_a_square(e) or (color_is_purple(e) and wrapped_in_a_cross(e))  
	condition_for_sending_left =  ((color_is_red(e) and (wrapped_in_a_triangle(e) or wrapped_in_a_circle(e))) or (color_is_orange(e) and wrapped_in_a_circle)) and divides_evenly_by(e,3)
	condition_for_sending_right =  color_is_red(e) and wrapped_in_a_cross(e) or (color_is_orange(e) and wrapped_in_a_square(e)) 
	return (condition_for_sending_down, condition_for_sending_left, condition_for_sending_right)

	
run_the_program(decision_making_function)
