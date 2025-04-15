'''
A pedometer treats walking 2,000 steps as walking 1 mile. 

Write a steps_to_miles() function that takes the number of steps as a parameter and returns the miles walked. 

The steps_to_miles() function raises a ValueError object with the message "Exception: Negative step count entered." when the number of steps is negative.
 Complete the main() program that reads the number of steps from a user, calls the steps_to_miles() function, and outputs the returned value from the 
 steps_to_miles() function. Use a try-except block to catch any ValueError object raised by the steps_to_miles() function and output the exception message.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print(f'{your_value:.2f}')

Ex: If the input of the program is:

5345
the output of the program is:

2.67
Ex: If the input of the program is:

-3850
the output of the program is:

Exception: Negative step count entered.
'''

# Function that converts steps to miles and raises a value error if the input number is less the zero. 

def steps_to_miles(steps):
       
    if steps < 0:
        raise ValueError("Exception: Negative step count entered.")
   
    steps_to_miles = steps / 2000
    
    print(f'\n Wow you walked {steps_to_miles:.2f} miles!')
    

if __name__ == '__main__':

# Opening message. 
    print("\nThis Program will change the amount of steps that you have taken in a day and will change them into miles!\n")

# While loop to keep the program going.    
    while True:
        
        try:
            # Input for the user.
            steps = int(input("\nEnter the amount of steps you've taken in a day! "))
        
            miles = steps_to_miles(steps)

            # Ends the loop. 
            break

        except ValueError:
            
            print("\nHow the heck did you walk negative steps! Try again!") 