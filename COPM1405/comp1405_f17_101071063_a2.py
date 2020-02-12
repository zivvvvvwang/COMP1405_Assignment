# ============================================================          
#                                                                      
# Student Name (as it appears on cuLearn): Ziwen Wang              
# Student ID (9 digits in angle brackets): <101071063>                  
# Course Code (for this current semester): COMP1405A                    
#                                                                    
# ============================================================  

import sys

# User's input 
number = int(sys.argv[1])

# Get second digit
print((number // 10) % 10)

# Find the index of '5' first appears 
print(sys.argv[1].find('5'))

# Get the sum of second digit and the index of '5'
result1 = ((number // 10) % 10 ) + (sys.argv[1].find('5'))

print(result1)

# Add 13 to result1
result2 = result1 + 13

print(result2)

# Add the next lowest number to result2 
result2 += (result2 -1)

print(result2)

# Subtract 10 from result2
result2 = result2 - 10

print(result2)

# Change result2 to foalt and divide by 2
result2 = float(result2 / 2)

print(result2)

# Subtract result1 from result2
result2 -= result1

print(result2)

# Add 89.5 to the result2
result2 += 89.5

# Change result2 to character and make upper 
final_result = chr(int(result2)).upper()

print(final_result)




