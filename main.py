from db_actions import deleting, inserting, selecting, updating

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