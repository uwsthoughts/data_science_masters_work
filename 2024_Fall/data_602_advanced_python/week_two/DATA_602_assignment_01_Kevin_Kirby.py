#Q1 Fix all the syntax and logical errors in the given source code 
#add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the 
# average is a high score. The high score variable holds the value that is considered a high score.

#Reasoning:I debated making this lowercase but decided to leave it uppercase and consider it a global variable for the program.
HIGH_SCORE = 95
 
# Get the test scores.
# Reasoning: uses a loop to grab the three scores while also adding an error for invalid inputs. The valid inputs are stored in a list and used to calculate the average furhter down
#The count starts at 1 and the loop will run until the count is greater than 3
testcount = 1
scores = []  #

while testcount <= 3: 
    try:
        score = float(input(f'Enter the score for test {testcount}: '))
        scores.append(score)  # Add the score to the list
        testcount += 1  # Increment test count after a valid score
    except ValueError:
        print("Invalid input. Please enter a number.")


# Calculate the average test score.
#Reasoning: The original code was missing parenthesis around the sum of the test scores, which would have caused test3 to be divided by 3 and then summed with test1 and test2.
#My fix uses the scores list created above to calculate the sum and then divides by the length of the list to get the average
average =  sum(scores) / len(scores)

# Print the average.
#Reasoning: I added a colon and a space to make it easier to read by allowing a space gap between the text and the number. Without the space before the end of the string, the number is attached to the text.
print('The average score is: ', average)

# If the average is a high score,
# congratulate the user.
#Reasoning: Given my decision to leave HIGH_SCORE as all caps, I changed HIGH_SCORE below to all caps so that the variable is called correctly. 
if average >= HIGH_SCORE:
    print("Congratulations! That's a great average score!")
else: 
    print('Your average score is: ' , average)

#Q2
#The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width of two rectangles and prints to the user the area of both rectangles. 

#Reasoning: I created a function that asks for the four inputs needed to calculate the area of the two rectangles and then calculates the area based on the calculate_area function
#define at the start. After the calculations are two print statements that show the areas of the two rectangles. After the function definition is the invocation of the function.
#A separate function wasn't technically needed since I don't need to use it later. However, I consider it a good habit to make functions out of things like these in case I do need them.

def get_rectangle_areas():
    def calculate_area(length, width):
        return length * width

    # getting length and width of first rectangle
    first_len = float(input("Enter the length of the first rectangle: "))
    first_width = float(input("Enter the width of the first rectangle: "))

    # getting length and width of second rectangle
    second_len = float(input("Enter the length of the second rectangle: "))
    second_width = float(input("Enter the width of the second rectangle: "))

    # Calculate areas
    area1 = calculate_area(first_len, first_width)
    area2 = calculate_area(second_len, second_width)

    # Print the areas
    print(f"The area of the first rectangle is: {area1}")
    print(f"The area of the second rectangle is: {area2}")

get_rectangle_areas()

#Q3 
#Ask a user to enter their first name and their age and assign it to the variables name and age. 
#The variable name should be a string and the variable age should be an int.  

#Reasoning: The name input takes the input and assigns it to the name variable. 
#For age, I wrapped the input in a While True loop with a try/except component so I can handle invalid inputs for age. I was 
#mainly interested in ensuring the age come become an integer of some sort. 
name = input("Enter your first name: ")

while True:
    try:
        age = int(input("Enter your age: "))
        break  # Break the loop if a valid integer is entered
    except ValueError:
        print("Please enter a valid age (an integer).")




#Using the variables name and age, print a message to the user stating something along the lines of:
# "Happy birthday, name!  You are age years old today!"

#Reasoning: It's a spin on what you asked for that alLowed me to add my personality flair.
print(f"Hi, {name}! The world keeps spinning! Happy birthday! You're {age} years old today, but you'll always be young to me.")
