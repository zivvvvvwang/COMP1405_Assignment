# ============================================================
#
# Student Name (as it appears on cuLearn): Ziwen Wang
# Student ID (9 digits in angle brackets): <101071063>
# Course Code (for this current semester): COMP1405A
#
# ============================================================

'''
This function will load a text file.

@ params      file_name,the name of the file to be loaded
@ return      an uppercase string containing the data read from the file

'''
def load_text(file_name):
    file_hndl = open(file_name,"r")
    file_data = file_hndl.read()
    file_hndl.close()
    return file_data.upper()

'''
This function will save data to a text file.

@ params      file_name,the name of the file to be saved
              file_data,the data to be written to the file
@ return      none

'''
def save_text(file_name,file_data):
    file_hndl = open(file_name,"w")
    file_hndl.write(file_data)
    file_hndl.close()
    

'''
This function will ask user to creat a new alphabet in any order

@ params      none
@ return      new alphabet that is user input 

'''
def cryptogram_alphabet():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_list = []
    flag = True
    user_input_alphabet = input("Please enter 26 letters in alphabet for any order! ").upper()
    if len(user_input_alphabet) != 26: # to check the user input is 26 letters or not.
        flag = False 
            
    for i in user_input_alphabet: # to check the user input have other letters or not.
        if ord(i) < 65 or ord(i) > 90:
            flag = False
            break
    
    for j in user_input_alphabet: # to chech the user input have same letters or not.
        if j not in alphabet_list:
            alphabet_list.append(i)
        else:
            flag = False
            break
    if flag :           # if user input is correct, return the user input alphabet
        return user_input_alphabet
    else:               # if user input is not correct, return origin alphabet
        print("Some error in your message, will output origin alphabet!")
        return alphabet
            

        
'''
This function is shifed to creat a new alphabet

@ params      shift_number,an inter number of shifted
@ return      change_value, a new alphabet  

'''
def caesar_cipher_alphabet(shift_number):
    time = 0
    change_value = ""
    while time < 26:
        # in ASCII A is 65 and Z is 90
        if 65+time <= 90-shift_number: 
            change_value += chr(65+time+shift_number)
        else:
            change_value += chr(65+time+shift_number-26)
        time += 1
    return change_value

'''
This function will use word which is user enterd, create a new alphabet.

@ params      keyword, the word which is user input
@ return      user_input_word + other_character, a new alphabet 

'''
def keyword_cipher_alphabet(keyword):
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    user_input_word = ""
    other_character=""

    count = 0
    for i in keyword:
        time = 0
        secend_time = 0
        count +=1
        for j in keyword:
            secend_time += 1
            if i == j:
                time +=1
            if time == 1 and count == secend_time:
                user_input_word+=i
    for t in alphabet:
        if t not in user_input_word:
            other_character += t
    return(user_input_word + other_character)
    

'''
This function will encrypte a word/sentence in a new form from a cryptograph

@ params      before_encode, the code that user want to encrypte
              cryptograph, a new cryptograph that user selected 
@ return      after_encide, the code that after encrypte 

''' 
def encode(before_encode,cryptograph):
    user_input_list = list(before_encode)
    cryptograph_list = list(cryptograph)
    after_encode_list = []
    after_encode = ""
    for i in user_input_list:
        location = ord(i) - 65
        if location>= 0 and location < 26:
            for j in range (len(cryptograph_list)):
                if j == location:
                    after_encode_list.append(cryptograph_list[j])
        else:
            after_encode_list.append(i)
    for i in after_encode_list:
        after_encode += i
    return after_encode


'''
*

@ params      before_decode, the code that user want to decrypte
              cryptograph, a new cryptograph that user selected
@ return      after_edecide, the code that after decrypte

'''   
def decode(before_decode,cryptograph):
    orgin_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    output = ""
    for i in before_decode:
        times = 0
        boolean_flag = True
        while boolean_flag:
            if times == 26:
                output += i
                boolean_flag = False
            elif i == cryptograph[times]:
                output += orgin_alphabet[times]
                boolean_flag = False
            else:
                times += 1
    return output


'''
This is the main function, responsible for the user interface.

@ params       none
@ return       none

'''
def main():
    init_text = ""
    current_text = ""
    current_alphabet = ""
    
    while True:
        menu = int(input("\ninitial text \t" + init_text+ "\ncurrent text \t" + current_text + "\nPlease choose one option. \n1. Load text in a file\n2. Save text in a file\n3. cryptogram alphabet\n4. Caesar cipher alphabet\n5. Keyword cipher alphabet\n6. Encode\n7. Decode\n8. Quit\n"))
        if menu <= 0 or menu > 8:
            print("Please choose an option between 1-7\n")
        if menu == 1:
            file_name = input("Please enter your file name! ")
            current_text = load_text(file_name)
            init_text = current_text
        elif menu == 2:
            if current_text == "":
                print("No text to save")
            else:
                save_text(input("Please enter file name! "),current_text)
        elif menu == 3:
            current_alphabet = cryptogram_alphabet()
        elif menu == 4:
            current_alphabet = caesar_cipher_alphabet(int(input("Please enter the number witch is you want to shift! ")))
        elif menu == 5:
            current_alphabet = keyword_cipher_alphabet(input("Please enter a key word! ").upper())
        elif menu == 6:
            if current_text == "":
                print("No current text! ")
            elif current_alphabet == "":
                print("No current alphabet! ")
            else:
                current_text = encode(current_text,current_alphabet)
        elif menu == 7:
            if current_text == "":
                print("No current text! ")
            elif current_alphabet == "":
                print("No current alphabet! ")
            else:
                current_text = decode(current_text,current_alphabet)
        elif menu == 8:
            break
    
main()
