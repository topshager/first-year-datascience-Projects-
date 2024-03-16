# Client-Side Application (client.py)
import socket

SERVER_HOST = #where the server is hosted
SERVER_PORT = #the port the server is listining on

#defining the send function of the server using socket
def send_request(request):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_HOST, SERVER_PORT))
        s.sendall(request.encode())
        response = s.recv(1024).decode()#definfing the server response
        print(response)



def check_phone_existence(phone):#checks phone number excists
    request = f"CHECK_PHONE_EXISTENCE|{phone}"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_HOST, SERVER_PORT))
        s.sendall(request.encode())
        response = s.recv(1024).decode()
        return response == "EXIST"

def register_customer():#registration of cusotomer if phone number does not excist
    fname = input("Enter customer's first name: ")
    sname = input("Enter customer's last name: ")
    address = input("Enter customer's address: ")
    phone = input("Enter customer's phone number: ")

    # Check if phone number already exists
    if check_phone_existence(phone):
        print("Customer with this phone number already exists.")
        return

    request = f"REGISTER_CUSTOMER|{fname}|{sname}|{address}|{phone}"
    send_request(request)

def register_equipment():#handles registration of equipment
    ename = input("Enter equipment name: ")
    etype = input("Enter equipment type (C for Construction, E for Electrical): ")
    request = f"REGISTER_EQUIPMENT|{ename}|{etype}"#defining the request that will be sent to server
    send_request(request)#send request to server side

def hire_equipment():#handles registration of equipment
    cust_phone = input("Enter customer's phone number: ")
    eId = input("Enter equipment ID: ")
    request = f"HIRE_EQUIPMENT|{cust_phone}|{eId}"
    send_request(request)#send reuest to server

def return_equipment():
    eId = input("Enter equipment ID: ")
    request = f"RETURN_EQUIPMENT|{eId}"
    send_request(request)

def display_menu():#GUI
    print("Menu:")
    print("1. Register Customer")
    print("2. Register Equipment")
    print("3. Hire Out Equipment")
    print("4. Return Equipment")
    print("5. Exit")

    choice = input("Enter your choice: ")#user input detection
    if choice == "1":
        register_customer()
    elif choice == "2":
        register_equipment()
    elif choice == "3":
        hire_equipment()
    elif choice == "4":
        return_equipment()
    elif choice == "5":
        print("Exiting program.")
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    while True:
        display_menu()
        if input("Do you want to continue (Y/N)? ").strip().upper() != 'Y':
            break
