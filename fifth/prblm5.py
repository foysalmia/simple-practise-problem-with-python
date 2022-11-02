import json

data = []

try:
    file = open('contacts.json')
    data = json.load(file)
    file.close()
    print("Successfully Loaded data from database")
except:
    print("No data in database")


def isDuplicate(name, number):
    isName = False
    isNumber = False
    for user in data:
        for dbname, dbphone in user.items():
            if dbname.upper() == name.upper():
                isName = True
            if dbphone == number:
                isNumber = True
    return isName, isNumber


while True:
    print("1. Create New Contact\n2. View Existing Contacts\n3. Exit ")
    option = input(" Enter Your Choice : ")
    if option == "1":
        contact = {}
        name = input(" Enter Your Contact Name : ")
        phone = input(f" Enter {name}'s Phone Number : ")
        isExist = isDuplicate(name, phone)
        if isExist[0] or isExist[1]:
            if isExist[0]:
                print('This person is already entered.')
            elif isExist[1]:
                print("This person's telephone number is already in the database")
            response = input(" Add anyway? ").upper()
            if response == "Y":
                contact[name] = phone
                data.append(contact)
            else:
                pass

        else:
            contact[name] = phone
            data.append(contact)

        with open("contacts.json", "w") as file:
            json.dump(data, file)
        file.close()
    elif option == "2":
        print()
        for user in data:
            for name, phone in user.items():
                print(name.upper(), phone)
        print()
    else:
        break
