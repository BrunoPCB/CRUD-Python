import sqlite3

class DB_Connection:
    _db_name = 'schema_oop_crud.db'

    def __init__(self):
        self.__connection = None
        self.__cursor = None
        self.__db_tablename = 'products_oop'

        self.__create_table()
    
    @property
    def tablename(self):
        return self.__db_tablename
    
    def __initialize_conn(self):
        try:
            self.__connection = sqlite3.connect(self._db_name)
        except sqlite3.Error:
            print("Erro opennig the Database.")
            return False
        self.__cursor = self.__connection.cursor()

        return self.__cursor

    def __finalize_conn(self):
        self.__cursor.close()
        self.__connection.close()    

    def __create_table(self):
        query = f"CREATE TABLE IF NOT EXISTS {self.__db_tablename}(" \
                 "prod_id INTEGER PRIMARY KEY AUTOINCREMENT, " \
                 "prod_name TEXT NOT NULL, " \
                 "prod_amount INTEGER, " \
                 "prod_description TEXT " \
                 ")"
        
        self.execute_cursor(query, None)


    def execute_cursor(self, query, data = None, result = None):
        self.__initialize_conn()        
        try:

            if result is not None:
                result_list = []
                for line in self.__cursor.execute(query):
                    result_list.append(line)
                
                return result_list
            
            elif data is None:
                return self.__cursor.execute(query)
            else:
                self.__cursor.execute(query, data)
                self.__connection.commit()

            return True
        except sqlite3.Error as err:
            print(f"An error occurred! Error: {err.args}")
            self.__connection.rollback()
        finally:
            self.__finalize_conn()
    