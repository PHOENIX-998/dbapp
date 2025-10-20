import mysql.connector

conn = mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="6000",
  database = "customer_management"
)
cursor = conn.cursor()

cname = input("Enter the customer name: ")
cmobile = int(input("Enter the mobile number: "))

sql = "INSERT INTO CUSTOMER (gname, gmobile) VALUES (%s,%s)"
cursor.execute(sql, (cname, cmobile))

conn.commit()
print("Customer added successfully!")

conn.close()
