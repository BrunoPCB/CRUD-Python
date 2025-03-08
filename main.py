# Main Interface
print("Welcome to our Products Database.\n"
      "What do you want to do?\n"
      "[I]nsert\n"
      "[S]elect\n"
      "[U]pdate\n"
      "[D]elete\n")

correct_input = True
while not correct_input:
    option = input(": ")

    correct_input = option.isalpha() and (option.lower() in 'isud')

    if option.lower() == 'i':
        # inserting
        ...
    elif option.lower() == 's':
        # selecting
        ...
    elif option.lower() == 'u':
        # updating
        ...
    elif option.lower() == 'd':
        # deleting
        ...