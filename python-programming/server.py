# Server-Side Application (server.py)
from datetime import date
import mysql.connector
import socket

# Connect to MySQL database
try:
    db = mysql.connector.connect(
        host="",
        user="",
        password="",
        database=""
    )
    print("Connected to MySQL database successfully.")
except mysql.connector.Error as err:
    print(f"Error connecting to MySQL database: {err}")
    exit()

cursor = db.cursor()

# Create a socket for server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)
print("listening for connections...")

# Function to check if phone number exists in the database
def check_phone_existence(phone):
    try:
        cursor.execute("SELECT COUNT(*) FROM customers WHERE phone = %s", (phone,))
        count = cursor.fetchone()[0]
        return count > 0
    except mysql.connector.Error as err:
        print(f"Error checking phone existence: {err}")
        return False

# Function to handle client requests
def handle_request(request):
    parts = request.split("|")
    command = parts[0]
    if command == "REGISTER_CUSTOMER":
        _, fname, sname, address, phone = parts
        if check_phone_existence(phone):
            return "PHONE_EXIST"
        else:
            try:
                cursor.execute("INSERT INTO customers (fname, sname, address, phone) VALUES (%s, %s, %s, %s)", (fname, sname, address, phone))
                db.commit()
                return "CUSTOMER_REGISTERED"
            except mysql.connector.Error as err:
                print(f"Error registering customer: {err}")
                return "ERROR"
    elif command == "REGISTER_EQUIPMENT":
        _, ename, etype = parts
        try:
            cursor.execute("INSERT INTO equipment (ename, type, dateAdded) VALUES (%s, %s, %s)", (ename, etype, date.today()))
            db.commit()
            return "EQUIPMENT_REGISTERED"
        except mysql.connector.Error as err:
            print(f"Error registering equipment: {err}")
            return "ERROR"
        pass
    elif command == "HIRE_EQUIPMENT":
        # Implement hire equipment logic
        _, cust_phone, eId = parts
        try:
            cursor.execute("SELECT custId FROM customers WHERE phone = %s", (cust_phone,))
            cust_id = cursor.fetchone()
            if cust_id:
                cursor.execute("INSERT INTO hire (custId, eId, dateHired) VALUES (%s, %s, %s)", (cust_id[0], eId, date.today()))
                db.commit()
                return "EQUIPMENT_HIRED"
            else:
                return "CUSTOMER_NOT_FOUND"
        except mysql.connector.Error as err:
            print(f"Error hiring equipment: {err}")
            return "ERROR"
        pass
    elif command == "RETURN_EQUIPMENT":
        _, eId = parts
        try:
            cursor.execute("UPDATE hire SET dateReturn = %s WHERE eId = %s AND dateReturn IS NULL", (date.today(), eId))
            db.commit()
            return "EQUIPMENT_RETURNED"
        except mysql.connector.Error as err:
            print(f"Error returning equipment: {err}")
            return "ERROR"
        pass
    elif command == "CHECK_PHONE_EXISTENCE":
        _, phone = parts
        if check_phone_existence(phone):
            return "EXIST"
        else:
            return "NOT_EXIST"
    else:
        return "INVALID_COMMAND"

# Main server loop
while True:
    # Accept client connection
    client_socket, client_address = server_socket.accept()
    print(f"Client connected: {client_address}")

    # Receive client request
    request = client_socket.recv(1024).decode()
    print("Received request:", request)

    # Handle client request
    response = handle_request(request)

    # Send response to client
    client_socket.sendall(response.encode())

    # Close client connection
    client_socket.close()

# Close database connection
db.close()
