from db_actions_POO import DB_Actions
from os import system

actions = DB_Actions()

def clear_terminal():
    system('cls')


def selecting():
    actions.selecting_from_DB()

def inserting():
    print("To insert data into the database, fill the following fields:")
    actions.name = input("Name: ")
    actions.amount = input("Amount: ")
    actions.descrition = input("Description: ")

    # Insert in the function that will insert into the database
    actions.inserting_into_DB()

def updating():
    print("To update, input what you want to change.")
    print("Fields let empty will not be updated.")
    actions.id = input("Product code: ")
    actions.name = input("Name: ")
    actions.amount = input("Amount: ")
    actions.descrition = input("Description: ")

    # Function that will update the data selected by the index, which is the product code.
    actions.updating_into_DB()

def deleting():
    print("To delete a record, you must input a product code.")
    print("If the product code does not be informed, nothing will be deleted.")
    actions.id = input("input the product code: ")

    # Function that will delete the code informed by the user.
    actions.deleting_into_DB()

# Main Interface
print("Welcome to our Products Database.\n"
      "What do you want to do?\n"
      "[I]nsert\n"
      "[S]elect\n"
      "[U]pdate\n"
      "[D]elete\n")

correct_input = False
while not correct_input:
    option = input(": ")

    correct_input = option.isalpha() and (option.lower() in 'isud')


if option.lower() == 'i':    
    clear_terminal()
    
    # inserting
    inserting()
    
elif option.lower() == 's':
    clear_terminal()

    # selecting
    selecting()

elif option.lower() == 'u':
    clear_terminal()
    
    # updating
    updating()

elif option.lower() == 'd':
    clear_terminal()

    # deleting
    deleting()
