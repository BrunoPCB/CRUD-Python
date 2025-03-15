from db_connection_POO import DB_Connection

class DB_Actions:
    def __init__(self):   
        self.__cursor = None
        self.__id = 0
        self.__name = ''
        self.__amount = 0
        self.__descrition = ''

        self.__db_conn = DB_Connection()
    
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, index):
        self.__id = index

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def amount(self):
        return self.__amount
    
    @amount.setter
    def amount(self, amount):
        self.__amount = amount

    @property
    def descrition(self):
        return self.__descrition
    
    @descrition.setter
    def descrition(self, descrition):
        self.__descrition = descrition


    def inserting_into_DB(self):               
        insert_query = f"INSERT INTO {self.__db_conn.tablename}(prod_name, prod_amount, prod_description) VALUES(?, ?, ?)"
        data = [self.name, self.amount, self.descrition]
    
        success = self.__db_conn.execute_cursor(insert_query, data)

        if success:
            print("Insertion successfully completed!")

    def updating_into_DB(self):  
        update_query_text, update_query_options = [], []
                 
        update_query_text.append(f"UPDATE {self.__db_conn.tablename} SET")
        
        data = []
        if self.name != '':
            update_query_options.append("prod_name = ?")
            data.append(self.name)
        
        if self.amount != 0:
            update_query_options.append("prod_amount = ?")
            data.append(self.amount)

        if self.descrition != '':
            update_query_options.append("prod_description = ?")
            data.append(self.descrition)

        query_options = ', '.join(update_query_options)
        update_query_text.append(query_options)

        update_query_text.append("WHERE prod_id = ?")

        update_query = ' '.join(update_query_text)
        data.append(self.id)
    
        success = self.__db_conn.execute_cursor(update_query, data)

        if success:
            print("Update successfully completed!")

    def deleting_into_DB(self):               
        delete_query = f"DELETE FROM {self.__db_conn.tablename} WHERE prod_id = ?"
        data = [self.id]
    
        success = self.__db_conn.execute_cursor(delete_query, data)

        if success:
            print("Deleting successfully completed!")

    def selecting_from_DB(self):
        select_query = f"SELECT * FROM {self.__db_conn.tablename}"
        select_list = []

        select_list = self.__db_conn.execute_cursor(select_query, None, select_list)
        if select_list:
            print('', 10 * '------')
            print(f"|{'Index'.center(10)} | {'Name'.center(10)} | {'Amount'.center(10)} | {'Description'.center(20)} |")
            print('', 10 * '------')

            for item in select_list:            
                index, product, amount, description = item
                print(f"|{str(index).center(10)} | {product.center(10)} | {str(amount).center(10)} | {description.center(20)} |")
            
            print('', 10 * '------')