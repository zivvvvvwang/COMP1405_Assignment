# ============================================================
#
# Student Name (as it appears on cuLearn): Ziwen Wang
# Student ID (9 digits in angle brackets): <101071063>
# Course Code (for this current semester): COMP1405A
#
# ============================================================

from comp1405_f17_assistant_a4 import *

question1 = ask_question('Do you have hair? ')
if question1.upper() == "YES":
	question2 = ask_question('Are you wear earring? ')
	if question2.upper() == "YES":
		question3 = ask_question('Are you wear glasses? ')
		if question3.upper() == "YES":
			question4 = ask_question('Are you wear moustache? ')
			if question4.upper() =="YES":
				make_a_guess("Jules")
			else: 
				make_a_guess("Dakota")
		else: 
			question4 = ask_question('Are you wear eyepatch? ')
			if question4.upper() == "YES":
				make_a_guess("Shawn")
			else:
				make_a_guess("River")
	else: 
		question3 = ask_question("Are you wear pipe?")
		if question3.upper() == "YES":
			question4 = ask_question('Are you wear moustache? ')
			if question4.upper() =="YES":
				make_a_guess("Kyle")
			else: 
				make_a_guess("Chris")
		else:
			question4 = ask_question('Are you wear eyepatch? ')
			if question4.upper() == "YES":
				make_a_guess("Alex")
			else: 
				make_a_guess("Monroe")
else: 
	question2 = ask_question('Do you have tattoo? ')
	if question2.upper() == "YES":
		question3 = ask_question('Are you wear eyepatch? ')
		if question3.upper() == "YES":
			question4 = ask_question('Are you wear tie? ')
			if question4.upper() =="YES":
				make_a_guess("Hunter")
			else: 
				make_a_guess("Gray")
		else: 
			question4 = ask_question('Are you wear glasses? ')
			if question4.upper() == "YES":
				make_a_guess("Emery")
			else: 
				make_a_guess("Kai")
	else: 
		question3 = ask_question("Are you wear hat? ")
		if question3.upper() == "YES":
			question4 = ask_question('Are you wear tie? ')
			if question4.upper() =="YES":
				make_a_guess("Quinn")
			else: 
				make_a_guess("Karter")
		else: 
			question4 = ask_question('Are you wear pipe? ')
			if question4.upper() == "YES":
				make_a_guess("Harper")
			else: 
				make_a_guess("Addison")

