from db_actions import deleting, inserting, selecting, updating, create_table
from os import system

def clear_terminal():
    system('cls')

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
    # inserting
    clear_terminal()
    
    inserting()
    ...
elif option.lower() == 's':
    # selecting
    selecting()
    ...
elif option.lower() == 'u':
    # updating
    updating()
    ...
elif option.lower() == 'd':
    # deleting
    deleting()
    ...