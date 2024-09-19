#Question 1:
# Write a program that prompts the user for a user_meal_choice: breakfast, lunch, or dinner. Then using if statements and else statements print the user a message recommending a user_meal_choice. For example, if the user_meal_choice was breakfast, you could say something like, “How about some bacon and eggs?”
# The user may enter something else in, but you only have to respond to breakfast, lunch, or dinner.


# asks user for user_meal_choice and turns it all lowercase to enure the loop works properly
user_meal_choice = input("Please enter a user_meal_choice. It can be breakfast, lunch, or dinner: ").lower()

# conditional loop that makes make based on inouts
if user_meal_choice == "breakfast":
    print("How about a yougurt parfait and a side of banana bread?")
elif user_meal_choice == "lunch":
    print("It's a good day for a Sweetgreen salad. Try their Caesar dressing to go with it")
elif user_meal_choice == "dinner":
    print("You can't go wrong with a Shake Shack burger")
else:
    print("Sorry, I only have ideas for breakfast, lunch, or dinner. I'll get smarter soon, I promise.")


# #Q2: The mailroom has asked you to design a simple payroll program that calculates a student employee’s gross pay, including any overtime wages. If any employee works over 20 hours in a week, the mailroom pays them 1.5 times their regular hourly pay rate for all hours over 20. 
# You should take in the user’s input for the number of hours worked, and their rate of pay.

# First, the function that calculates the different types of hourly rates. 
def gross_pay_calc(hours_worked, hourly_rate):
    reg_hrs = 20
    ot_rate = 1.5

    # this is the part that checks for OT hours and pays accordingly
    if hours_worked > reg_hrs:
        ot_hrs = hours_worked - reg_hrs
        reg_pay = reg_hrs * hourly_rate
        ot_pay = ot_hrs * hourly_rate * ot_rate
        gross_pay = reg_pay + ot_pay
    else:
        gross_pay = hours_worked * hourly_rate
    return gross_pay

# back-to-back inputs that ask user for hours and rate so the gross_pay_calc can pick them up
hours_worked = float(input("How many hours did you work? "))
hourly_rate = float(input("How much are you paid an hour? "))

# calculates gross pay using inputs above as parameters in function
gross_pay = gross_pay_calc(hours_worked, hourly_rate)
print(f"Total gross pay is: ${gross_pay:.2f}")

# Q3: Write a function named times_ten. The function should accept an argument and display the product of its argument multiplied times 10.

#simple but does the trick
def times_ten(num):
    math_logic = num * 10
    print(f"The result of {num} times 10 is {math_logic}")

# Example use - expected result is 50
times_ten(5)  

# SQ4: Find the errors, debug the program, and then execute to show the output.

#provided code to fix:
def main()
      Calories1 = input( "How many calories are in the first food?")
      Calories2 = input( "How many calories are in the first food?")
      showCalories(calories1, calories2)

def showCalories()   
   print(“The total calories you ate today”, format(calories1 + calories2,.2f))


#1. The main() definition needs to include colons after it so it says main():
#2. Variable names Calories1 and Calories2 are capitalized, but when passed to showCalories it's done as lowercase calories1 and calories2. Python is case sensitive.
#3 The showCalories() function needs to accept two arguments for the print statement to work properly, otherwise it won't have anything to print
#4 String Formatting Issue: 
#4 The formatint inside the final print steatement is wrong. It needs to be 2 decimal places by using an f-string.

# Corrected code:
def main():
    calories1 = float(input("How many calories are in the first food? "))
    calories2 = float(input("How many calories are in the second food? "))
    showCalories(calories1, calories2)

def showCalories(calories1, calories2):
    total_calories = calories1 + calories2
    print(f"The total calories you ate today: {total_calories:.2f}")

main()

# Q5: Write a program that uses any loop (while or for) that calculates the total of the following series of numbers:
#          1/30 + 2/29 + 3/28 ............. + 30/1

def series_calc():
    total = 0.0

    # loop through whole series by using the inclusive, exclusive model for range inouts
    for i in range(1, 31):
        total += i / (31 - i)
    
    # print total
    print(f"Series total: {total:.4f}")

# invoke function for demo
series_calc()

# Q6: Write a function that computes the area of a triangle given its base and height.
# The formula for an area of a triangle is:
# AREA = 1/2 * BASE * HEIGHT

#takes base and height as parameters and then calculates area using provided formula
def tri_area(base, height):
    area = 0.5 * base * height
    return area

# example of how to invoke
base = float(input("Triangle base? "))
height = float(input("Triangle height?: "))

# Call the function and display the result
area = tri_area(base, height)
print(f"The area of the triangle is: {area:.2f}")








