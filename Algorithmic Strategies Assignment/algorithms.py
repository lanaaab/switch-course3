'''
Largest of 3
Write a function that receives 3 numbers and return the biggest one.
You are not allowed to use any functions including built in ones.
'''

def find_largest_number(num1, num2, num3):
    largest_num = num1
    if num2 > largest_num:
        largest_num = num2
    if num3 > largest_num:
        largest_num = num3
    return largest_num
        
    
 
''' 
Word Score:
Given a string of words, you need to find the highest scoring word.
Each letter of a word scores points according to it's position in the alphabet: a = 1, b = 2, c = 3 etc.
You need to return the highest scoring word as a string.
If two words score the same, return the word that appears earliest in the original string.
All letters will be lowercase and all inputs will be valid.
'''

def find_highest_scoring_word(sentence):
    max_word_score = 0
    max_word = ""
    
    for word in sentence.split():
        word_score = 0
        for letter in word:
            word_score += ord(letter.lower()) - ord('a') + 1
            
        if word_score > max_word_score:
            max_word_score = word_score
            max_word = word
            
    return max_word
