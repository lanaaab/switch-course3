def palindrome_check(entered_input):
    entered_input_rev = entered_input[::-1]
    if(entered_input == entered_input_rev):
        return True
    return False
    
    
def lowercase_check(entered_input):
    if(entered_input.islower()):
        return True
    return False
    
    
def digit_check(entered_input):
    if(entered_input.isdigit()):
        return True
    return False
    
    
def length_check(entered_input):
    str_len = len(entered_input)
    if(str_len > 15):
        return True
    return False
    
    
def empty_check(entered_input):
    if(entered_input == ''):
        return True
    return False    


exit_flag = False
answer = False

while(not exit_flag):
    print("The available operations are: ")
    print("1 - Palindrome: Check if the input is palindrome ")
    print("2 - Lower: Check if all characters in the input are lowercase ")
    print("3 - Digit: Check if all characters in the input are digits ")
    print("4 - Long: Check if the input length is longer than 15 ")
    print("5 - Empty: Check if the input is empty ")
    print("6 - Exit: Exit successfully from the application ")
    
    op_num = input("Please enter the number of the operation you choose: ")
    while(True):
        try:
            op_num = int(op_num)
            if(op_num >= 1 and op_num <= 6):
                break
            else:
                op_num = input("Please enter a valid number between 1 snd 6: ")
        except:
            op_num = input("Please enter a valid number: ")
            
    if(op_num == 6):
        exit_flag = True
        continue
         
         
    entered_input = input("Enter an input: ")
    
    if(op_num == 1):
        answer = palindrome_check(entered_input)
        if(answer):
            print(f"{entered_input} is a palindrome.\n")
        else:
            print(f"{entered_input} is not a palindrome.\n")
        
        
    if(op_num == 2):
        answer = lowercase_check(entered_input)
        if(answer):
            print("All characters are lowercase.\n")
        else:
            print("Not all characters are lowercase.\n")
        
        
    if(op_num == 3):
        answer = digit_check(entered_input)
        if(answer):
            print("All characters are digits.\n")
        else:
            print("Not all characters are digits.\n")
        
        
    if(op_num == 4):
        answer = length_check(entered_input)
        if(answer):
            print("The input length is longer than 15.\n")
        else:
            print("The input length is shorter or equal to 15.\n")
       
        
    if(op_num == 5):
        answer = empty_check(entered_input)
        if(answer):
            print("The input is empty.\n")
        else:
            print("The input is not empty.\n")
    
  
    
    
    