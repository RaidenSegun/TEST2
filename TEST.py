import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def open_connection(self):
        self.connection = sqlite3.connect(self.db_name)  
        print("Соединение с базой данных установлено.")

    def close_connection(self):
        if self.connection:
            self.connection.close()  
            print("Соединение с базой данных закрыто.")

    def execute_query(self, query):
        cursor = self.connection.cursor()  
        cursor.execute(query)  
        self.connection.commit()  
        return cursor  


    def find_user_by_name(self, name):
        search_query = f"SELECT * FROM users WHERE name = '{name}';" 
        cursor = self.execute_query(search_query)  
        return cursor.fetchall() if cursor else None  

    def execute_transaction(self):
        cursor = self.connection.cursor()  
        cursor.execute("INSERT INTO users (name, role) VALUES ('Яхье Шах', 'customer');")
        cursor.execute("INSERT INTO users (name, role) VALUES ('Нурсултан Назарбаев', 'admin');")
        self.connection.commit()  
        print("Транзакция успешно выполнена!")


if __name__ == "__main__":
    db_manager = DatabaseManager("example.db")
    db_manager.open_connection()
    db_manager.execute_query("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        role TEXT NOT NULL
    );
    """)

    db_manager.execute_transaction()
    users = db_manager.find_user_by_name("Яхье Шах")
    print("Найденные пользователи:", users)
    db_manager.close_connection()