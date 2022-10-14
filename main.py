pali = input("please enter a palindrome ")
    #getting the user input

pali = str.casefold(pali)
    #making the input lowercase

pali1 = reversed(pali)
    #making the user input reversed

if list(pali1) == list(pali):
    print("True")
else:
    print("False")
    #if else statement to check if the user input is a palindrome

