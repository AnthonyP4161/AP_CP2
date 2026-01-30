#AP 1st, Random Password Generator
import random
def main():
    lower_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    upper_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    spec_char_list = ["!","@","#","$","%","^","&","*","(",")","?","/","\\","|"]
    length = int(input("How many characters does the password need to be(Please enter digits, not words)\nInput: "))
    lower = input("Does the password need lowercase letters (Y/N)\nInput: ").upper().strip()
    upper = input("Does the password need uppercase letters (Y/N)\nInput: ").upper().strip()
    num = input("Does the password need numbers (Y/N)\nInput: ").upper().strip()
    spec_char = input("Does the password need special characters (Y/N)\nInput: ").upper().strip()
    password = ""
    for i in range(0,4):
        password = ""
        while True:
            rand = random.randint(1,4)
            if rand == 1:
                if lower == "Y":
                    char = random.choice(lower_list)
                    password = password+char
            elif rand==2:
                if upper=="Y":
                    char = random.choice(upper_list)
                    password = password+char
            elif rand==3:
                if num=="Y":
                    char = str(random.randint(0,9))
                    password = password+char
            elif rand==4:
                if spec_char=="Y":
                    char = random.choice(spec_char_list)
                    password = password+char
            if len(password)==length:
                print(f"{i+1}: {password}")
                break
            
while True:
    choice = input("Select your choice by entering the number associated\n1: Generate Passwords\n2: Exit\nInput: ")
    if choice == "1":
        main()
    elif choice == "2":
        break
    else:
        print("Pretty please choose a valid option")