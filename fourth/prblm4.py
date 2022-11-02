import json

data = []

try:
    file = open('contacts.json')
    data = json.load(file)
    file.close()
    print("Successfully Loaded data from database")
except:
    print("No data in database")

while True:
    print("1. Create New Contact\n2. View Existing Contacts\n3. Exit ")
    option = input(" Enter Your Choice : ")
    if option == "1":
        contact = {}
        name = input(" Enter Your Contact Name : ")
        phone = input(f" Enter {name}'s Phone Number : ")
        contact[name] = phone
        data.append(contact)

        with open("contacts.json", "w") as file:
            json.dump(data, file)
    elif option == "2":
        print()
        for user in data:
            for name, phone in user.items():
                print(name.upper(), phone)
        print()
    else:
        break
