def inserting():
    print("To insert data into the database, fill the following fields:")
    product_name = input("Name: ")
    product_amount = input("Amount: ")
    product_description = input("Description: ")

    # Insert in the function that will insert into the database


def selecting():
    amount_to_retrive = input("How much data do you want to retrieve: ")    

    # Function that will retrieve the data from the database

def updating():
    print("To update, input what you want to change.")
    print("Fields let empty will not be updated.")
    index = input("Product code: ")
    product_name = input("Name: ")
    product_amount = input("Amount: ")
    product_description = input("Description: ")

    # Function that will update the data selected by the index, which is the product code.

def deleting():
    print("To delete a record, you must input a product code.")
    print("If the product code does not be informed, nothing will be deleted.")
    product_code = input("input the product code: ")

    # Function that will delete the code informed by the user.