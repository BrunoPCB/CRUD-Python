from db_connection import create_table, inserting_into_DB, deleting_into_DB, updating_into_DB

def inserting():
    success = create_table()

    if not success:
        return

    print("To insert data into the database, fill the following fields:")
    product_name = input("Name: ")
    product_amount = input("Amount: ")
    product_description = input("Description: ")

    # Insert in the function that will insert into the database
    inserting_into_DB(product_name, product_amount, product_description)


def selecting():
    success = create_table()

    if not success:
        return    

    amount_to_retrive = input("How much data do you want to retrieve: ")    

    # Function that will retrieve the data from the database

def updating():
    success = create_table()

    if not success:
        return    

    print("To update, input what you want to change.")
    print("Fields let empty will not be updated.")
    index = input("Product code: ")
    product_name = input("Name: ")
    product_amount = input("Amount: ")
    product_description = input("Description: ")

    # Function that will update the data selected by the index, which is the product code.
    updating_into_DB(product_name, product_amount, product_description, index)

def deleting():
    success = create_table()

    if not success:
        return    

    print("To delete a record, you must input a product code.")
    print("If the product code does not be informed, nothing will be deleted.")
    product_code = input("input the product code: ")

    # Function that will delete the code informed by the user.
    deleting_into_DB(product_code)