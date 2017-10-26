import json

address_book_dict = {}
while True:
    name = input('Name: ')
    if name == 'exit':
        break
    else:
        phone = input('Phone: ')
        address_book_dict[name] = phone

address_book_file = open('address_book.txt', 'w')
address_book_json = json.dumps(address_book_dict)
address_book_file.write(address_book_json)
address_book_file.close()