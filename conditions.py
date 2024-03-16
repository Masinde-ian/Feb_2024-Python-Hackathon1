# Python Conditional Statements 
#example is https://plpacademy.powerlearnproject.org/course-module/62fbec9d28ac4762bc524f92/week/62fe1efd28ac4762bc524f9c/lesson/62fe1fbd28ac4762bc524f9f



# Create a Python program that:


# - Prompts a user to enter their age.
# - Uses a conditional statement to check if the age is greater than or equal to 18.
# - Prints "You are eligible to vote" if true, otherwise "You are not eligible to vote."
def vote(age):
    '''
    Arguments: int(age) a persons age. 
    Returns: str() message confirming to the user if they are eligible to vote.

    '''
    if age >= 18:
        return "You are eligible to vote."
    else:
        return "You are not eligible to vote." 
    
age=int(input("Please enter your age: "))
print(vote(age))
