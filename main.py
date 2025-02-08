import sqlite3

# Подключение к базе данных SQLite
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Создание таблицы "Customers"
c.execute('''
CREATE TABLE Customers (
    CustomerID INTEGER PRIMARY KEY,
    CustomerName TEXT
)
''')

# Создание таблицы "Orders"
c.execute('''
CREATE TABLE Orders (
    OrderID INTEGER PRIMARY KEY,
    OrderDate DATE,
    CustomerID INTEGER,
    FOREIGN KEY(CustomerID) REFERENCES Customers(CustomerID)
)
''')

# Вставка данных в таблицу "Customers"
c.execute("INSERT INTO Customers (CustomerID, CustomerName) VALUES (1, 'John')")
c.execute("INSERT INTO Customers (CustomerID, CustomerName) VALUES (2, 'Lisa')")
c.execute("INSERT INTO Customers (CustomerID, CustomerName) VALUES (3, 'David')")
c.execute("INSERT INTO Customers (CustomerID, CustomerName) VALUES (4, 'Emily')")

# Вставка данных в таблицу "Orders"
c.execute("INSERT INTO Orders (OrderID, OrderDate, CustomerID) VALUES (1, '2022-01-01', 1)")
c.execute("INSERT INTO Orders (OrderID, OrderDate, CustomerID) VALUES (2, '2022-02-01', 2)")
c.execute("INSERT INTO Orders (OrderID, OrderDate, CustomerID) VALUES (3, '2022-03-01', 3)")
c.execute("INSERT INTO Orders (OrderID, OrderDate, CustomerID) VALUES (4, '2022-04-01', 5)") # Заказ для несуществующего клиента

# c.execute('''
# SELECT Customers.CustomerID, Customers.CustomerName, Orders.OrderID, Orders.OrderDate
# FROM Customers
# FULL OUTER JOIN Orders ON Customers.CustomerID = Orders.CustomerID''')

# # Получение результатов Full Outer Join
# result_full_outer_join = c.fetchall()
#
# # Вывод результата Full Outer Join
# print("Результат Full Outer Join:")
# for row in result_full_outer_join:
#     print(row)
#

c.execute('''
SELECT Customers.CustomerID, Customers.CustomerName, Orders.OrderID, Orders.OrderDate
FROM Customers
FULL OUTER JOIN Orders ON Customers.CustomerID = Orders.CustomerID
WHERE Orders.CustomerID IS NULL OR Customers.CustomerID IS NULL
''')

# Получение результатов Full Outer Excluding Inner Join
result_full_outer_excluding_inner_join = c.fetchall()

# Вывод результата Full Outer Excluding Inner Join
print("\nРезультат Full Outer Excluding Inner Join:")
for row in result_full_outer_excluding_inner_join:
    print(row)

# Закрытие соединения с базой данных
conn.close()



