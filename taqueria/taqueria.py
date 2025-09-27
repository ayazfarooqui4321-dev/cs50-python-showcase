#Requirements:
#Enable users to place an order
#prompt users for items from menu, one item per line
#keep outputting items until ctrl+d
#After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places.
#Treat the user’s input case insensitively.
#Ignore any input that isn’t an item
#Assume that every item on the menu will be titlecased.'Hello world'.title()

#copied and pasted the menu from the coding problem
def main():
    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
    #start from zero
    total = 0.0
# using while because we don't know the end. You don’t know how many items the user will type. A while loop is the way to repeat indefinitely until external stop.
    while True:
        try:
            #Meets the requirement of striping all empty spaces to be taken out and title like the First letter of the each word is capital
            item = input("Item: ").strip().title()
            #Keep going until a cntrl+D is invoked and then print an empty line
        except EOFError:
            print()
            break
        #If the item is match from the menu, add the total(all selected so far) and display it with two decimal
        if item in menu:
            total += menu[item]
            print(f"Total: ${total:.2f}")

if __name__ == "__main__":
    main()
