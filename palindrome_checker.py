#!/usr/bin/env python3

"""
palindrome_checkerpy
Write a program palindrome_checker.py that includes a class definition for PalindromeChecker that includes at least two methods:

a setter method setStrictMode() that takes a boolean value as input, which turns "strict mode" on and off
a boolean method isPalindrome(phrase) that takes a phrase as a parameter and returns true if the phrase is a palindrome, and false if it isn't. This method should use a Deque object to check the expression, and return True if the expression entered is a valid palindrome.
If "strict mode" is on, a palindrome will only be indicated if the phrase reads exactly the same, forwards and backwards, including spaces, punctuation, and case (upper and lower). If "strict mode" is off, then spaces, punctuation, and different cases are allowed, and the phrase will be identified as a palindrome because their letters all match.

You may wish to write an additional helper method sanitize(phrase) that will produce a new, "sanitized" version of a phrase that doesn't have any spaces, punctuation, or uppercase letters in it. This method can be useful when "strict mode" is off.

The main() function in the palindrome_checker.py can be used to perform a series of tests.


"""
from atds import * 
__author__ = "Sabrina Zhang"
__version__ = "2023-2-23"

def setStrictMode():
    """
    a setter method setStrictMode() that takes a boolean value as input, which turns "strict mode" on and off
    """
    global strict_mode
    strict_mode = True
    
def sanitize(phrase, newexpr):
    """You may wish to write an additional helper method sanitize(phrase) that will produce a new, "sanitized" version of a phrase that doesn't have any spaces, punctuation, or uppercase letters in it. This method can be useful when "strict mode" is off."""

    newexpr = phrase.replace('.', '')
    newexpr = phrase.replace(',', '')
    newexpr = phrase.replace(';', '')
    newexpr = phrase.replace('\'', '')
    newexpr = phrase.replace(':', '')
    newexpr = phrase.replace('!', '')
    newexpr = phrase.replace('?', '')
    return newexpr
    """
    for l in phrase:
            if l != " " and l != "," and l != "." and l != "'":
                newexpr += l
    """

def isPalindrome(phrase):
    """
    a boolean method isPalindrome(phrase) that takes a phrase as a parameter and returns true if the phrase is a palindrome, and false if it isn't. This method should use a Deque object to check the expression, and return True if the expression entered is a valid palindrome.
    """
    try:
        if strict_mode:
            b = True
    except:
        b = False
    even = False
    expr = ""
    #when in strict mode, must 
    if b == False:
        expr = sanitize(phrase, expr)
        
    else:
        expr = phrase

    if (len(phrase)%2 == 0):
        even = True
    i = 0
    s = Deque()
    for l in expr:
        # going through each letter in the expression 
        letter = l.lower()
        
        half = len(expr)/2    
        
        if i < int(half):
            
            s.add_rear(letter)
            i+=1
        elif even == True and i >= int(half):
            pal = s.remove_rear()
            #print(" palindrome " + letter)
            if(pal != letter):
                return False
            i+=1
        elif even == False and i > int(half):
            #print(" palindrome " + letter)
            pal = s.remove_rear()
            
            if(pal != letter):
                return False
            i+=1
        else:
            i+=1

    return s.is_empty()

def main():
    print("Running the palindrome checker!")
    print("Check: A man, a plan, a canal: PANAMA!")
    if(str(isPalindrome("A man, a plan, a canal: PANAMA!"))):
        print("Is a palindrome")
    else:
        print("Not a palindrome")
    print("Check: Hannah")
    if(str(isPalindrome("Hannah"))):
        print("Is a palindrome")
    else:
        print("Not a palindrome")
    
    print("Check: race car")
    if(str(isPalindrome("race car"))):
        print("Is a palindrome")
    else:
        print("Not a palindrome")
    
    print("Entering strict mode... ")
    setStrictMode()
    print("Check on strict: A man, a plan, a canal: PANAMA!")
    if(str(isPalindrome("A man, a plan, a canal: PANAMA!"))):
        print("Is a palindrome")
    else:
        print("Not a palindrome")

    print("Check on strict: Hannah")
    if(str(isPalindrome("Hannah"))):
        print("Is a palindrome")
    else:
        print("Not a palindrome")
    
    print("Check on strict: race car")
    if(str(isPalindrome("race car")) == True):
        print("Is a palindrome")
    else:
        print("Not a palindrome")


    


if __name__ == "__main__":
    main()

