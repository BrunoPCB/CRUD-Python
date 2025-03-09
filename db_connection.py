import sqlite3

def create_conn():
    return sqlite3.connect("products.db")

def create_cursor(connection):
    return connection.cursor()

def terminate_conn(connection, cursor):
    cursor.close()
    connection.close()

def execute_cursor(sql_query_param, success_msg_param=""):    
    connection = create_conn() 
    cursor = create_cursor(connection) 

    try:
        data = None
        if type(sql_query_param) is tuple:
            sql_query, data = sql_query_param
        else:
            sql_query = sql_query_param

        if data is None:
            cursor.execute(sql_query)
        else:
            cursor.execute(sql_query, data)
            
        connection.commit()

        if success_msg_param != "":
            print(success_msg_param)
        else:
            print("Exectuion was succeded.")


        return True
    except Exception as exc:
        print("An exception occurred")
        print(f"""Exception info: \n
            {exc}""")
        return False
    except sqlite3.Error as error:
        print("An error occurred.")
        print(f"""Erro info: \n
            Name: {error.sqlite_errorname}\n
            Code: {error.sqlite_errorcode}""") 
        return False
    finally:
        terminate_conn(connection=connection, cursor=cursor)

__db_tb_products = 'products'

# Using args variable to pass my arguments
def create_table():
    db_create = f"CREATE TABLE IF NOT EXISTS {__db_tb_products}(" \
                "prod_id INTEGER PRIMARY KEY AUTOINCREMENT, " \
                "prod_name TEXT NOT NULL, " \
                "prod_amount INTEGER, " \
                "prod_description TEXT " \
                ")"
    
    success_msg = f"The table {__db_tb_products} was successfully created!"

    return execute_cursor(db_create, success_msg_param=success_msg)

def inserting_into_DB(*prod_info_param):
    
    db_insert = (f"INSERT INTO {__db_tb_products}(prod_name, prod_amount, prod_description)" \
                "VALUES (?, ?, ?)", tuple(prod_info_param))
    
    success_msg = f"The insertion was completed!"

    return execute_cursor(db_insert, success_msg_param=success_msg)
    

def deleting_into_DB(*prod_info_param):
    db_delete = (f"DELETE FROM {__db_tb_products} WHERE prod_id = ?", tuple(prod_info_param))
    
    success_msg = f"The item was deleted!"

    return execute_cursor(db_delete, success_msg)

def updating_into_DB(*prod_info_param):
    db_update = (f" UPDATE {__db_tb_products} SET " \
                "prod_name = ?, " \
                "prod_amount = ?, " \
                "prod_description = ?" \
                "WHERE prod_id = ?", 
                tuple(prod_info_param))
    
    success_msg = f"The item was updated!"

    return execute_cursor(db_update, success_msg)