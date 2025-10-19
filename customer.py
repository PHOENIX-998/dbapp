import sqlite3

conn = sqlite3.connect('CUSTOMER_MANAGEMENT')
cursor = conn.cursor()

cname = input("Enter the customer name: ")
cmobile = int(input("Enter the mobile number: "))

# ✅ Use placeholders for variables
cursor.execute("INSERT INTO CUSTOMER (gname, gmobile) VALUES (?, ?)", (cname, cmobile))

conn.commit()
print("Customer added successfully!")

conn.close()
