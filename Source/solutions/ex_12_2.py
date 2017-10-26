import json

address_book_file = open("address_book.txt", "r")
address_book = json.load(address_book_file)
address_book_file.close()


def insert_person():
    name = input("Pleas enter a name: ")
    phone_number = input("Please enter a phone number: ")
    address_book[name] = phone_number


def search_person():
    name = input("Please provide the name of the person: ")
    if name in address_book:
        print("The phone number of " + name + " is: " + address_book[name])
    else:
        print("Person not found")


def remove_person():
    name = input("Please provide the name of the person you want to remove: ")
    if name in address_book:
        del (address_book[name])
        print("Successfully removed " + name)
    else:
        print("Person not found")


print("What do you want to do?")
print("Enter 'add' to add a new person to the address book")
print("Enter 'search' to lookup a phone number")
print("Enter 'remove' to remove a person from the address book")
print("Enter 'exit' to quit")

while True:
    action = input(">>> ")
    if action == "add":
        insert_person()
    if action == "search":
        search_person()
    if action == "remove":
        remove_person()
    if action == "exit":
        break

print("Bye Bye")

address_book_file = open("address_book.txt", "w")
address_book_file.write(json.dumps(address_book))
address_book_file.close()
