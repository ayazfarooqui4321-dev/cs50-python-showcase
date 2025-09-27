def main():
    while True: #Start a loop for reprompting the user until a proper user input
        fraction = input("Fraction: ").strip() #Requirement: Take user input
        try: #Keep trying until a valid/invalid user input
            x, y = fraction.split("/") #Split it on '/' to get values for int 'x' & 'y'
            x = int(x)
            y = int(y)
            #Requrement: Check for divide by zero OR values of 'x' being greater than 'y' OR 'x' or 'y' are less than '0'
            if y == 0 or x > y or x < 0 or y < 0:
                continue  # Requirement: If the condition met in above check, prompt the user again for a valid input
            percentage = round((x / y) * 100) #Requirement to covert to percentage and round to the nearest integer
            if percentage <= 1: #Requirement: Check to see if percentage is < or == to 1%, gas tank is on 'E', so print it
                print("E")
            elif percentage >= 99: #Requirement: Check to see if percentage is > or == to 99%, gas tank is full, so print it
                print("F")
            else: #Otherwise, just print all fractions as as their percentages and quit the program. No need to reprompt the user
                print(f"{percentage}%") # use the f string to print with '%' sign appended at the end
            break  # Exit loop after valid input and output
        except (ValueError, ZeroDivisionError): #Requirement: Catch errors like divide by zero or any value error and prompt user again
            continue  # Continue because of invalid input reprompt user
main()

