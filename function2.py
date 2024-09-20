### Contact Book
# Create a contact book where users can add, view, and delete contacts.

# Instructions:

# Define three functions: add_contact(), view_contacts(), and delete_contact().
# Use a dictionary to store contact names as keys and phone numbers as values.
# Let the user perform different operations (add, view, or delete) in a loop.


# single responsibilty

contact_notbook = {}

def add_contant(name, value):
    contact_notbook[name] = value

def view_contact(name):
    return contact_notbook.get(name)

def delete_contact(name):
    del contact_notbook[name]


while True:
    print("Please select an operation between add, view delete contant")

    op = input("Please eneter: \n")

    if op == "add":
        name = input("please insert name: \n") #line break
        value = input("please insert value: \n")
        add_contant(name, value)  
    elif op == "view":
        name = input("please insert name: \n")
        print(view_contact(name))
    elif op == "delete":
        name = input("please insert name: \n")
        print(delete_contact(name))
    else:
        break
    







exit()



############################# ANSWER ############################# 

# contacts = {}

# def add_contact(name, phone):
#     contacts[name] = phone
#     print(f"Contact {name} added.")

# def view_contacts():
#     if contacts:
#         for name, phone in contacts.items():
#             print(f"{name}: {phone}")
#     else:
#         print("No contacts available.")

# def delete_contact(name):
#     if name in contacts:
#         del contacts[name]
#         print(f"Contact {name} deleted.")
#     else:
#         print(f"Contact {name} not found.")

# while True:
#     print("\nOptions:")
#     print("1. Add Contact")
#     print("2. View Contacts")
#     print("3. Delete Contact")
#     print("4. Exit")

#     choice = input("Choose an option: ")

#     if choice == '4':
#         break

#     if choice == '1':
#         name = input("Enter contact name: ")
#         phone = input("Enter contact phone: ")
#         add_contact(name, phone)
#     elif choice == '2':
#         view_contacts()
#     elif choice == '3':
#         name = input("Enter the name to delete: ")
#         delete_contact(name)
#     else:
#         print("Invalid choice")
