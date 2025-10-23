import mysql.connector

class CustomerDatabase:
    def __init__(self):
        # Establish database connection
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="6000",
            database="customer_management"
        )
        self.cursor = self.conn.cursor()

    def add_customer(self):
        cname = input("Enter the customer name: ").strip()
        cmobile = input("Enter the mobile number: ").strip()

        # Validate mobile number
        if not cmobile.isdigit():
            print("Error: Please enter digits only.")
            self.close()
            return

        # Check for duplicate mobile
        self.cursor.execute("SELECT COUNT(*) FROM CUSTOMER WHERE gmobile = %s", (cmobile,))
        exists = self.cursor.fetchone()[0]

        if exists > 0:
            print("Error: This mobile number already exists in the database.")
            self.close()
            return

        # Insert record safely
        try:
            sql = "INSERT INTO CUSTOMER (gname, gmobile) VALUES (%s, %s)"
            self.cursor.execute(sql, (cname, cmobile))
            self.conn.commit()
            print("Customer added successfully!")
        except mysql.connector.Error as e:
            print("Database Error:", e)
        finally:
            self.close()

    def close(self):
        # Close the connection safely
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("Database connection closed.")

class UpdateCustomer:
    def __init__(self):
        # Establish database connection
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="6000",
            database="customer_management"
        )
        self.cursor = self.conn.cursor()

    def add_customer(self):
        cname = input("Enter the customer name: ").strip()
        cmobile = input("Enter the mobile number: ").strip()

        # Validate mobile number
        if not cmobile.isdigit():
            print("Error: Please enter digits only.")
            self.close()
            return
# Run program
if __name__ == "__main__":
    db = CustomerDatabase()
    db.add_customer()
