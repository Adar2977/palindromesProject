pali = input("please enter a palindrome ")
    #getting the user input

pali = str.casefold(pali)
    #making the input lowercase
def revFunction(pali):

        return pali[::-1]
    #function that makes the user input reversed
    #The return statement makes the string move in reverse. And returns the input backwards

def palindrome(pali):
        if revFunction(pali) == pali:
                print("True")
        else:
                print("False")

        return palindrome
#function that checks if the input is a palindrome

print(palindrome(pali))
#printing out the palindrome function



