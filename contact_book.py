import json

class contact_book:

    def __init__(self):
        try:
            f = open("contacts.json")
            y = json.loads(f.read())
            self.contacts = y

        except FileNotFoundError:
            self.contacts = {}

    def addcontacts(self):
        name = input("Enter you're name..\n")
        phone_no = input("Enter you're phone number..\n")
        self.contacts[name] = phone_no

    def viewcontacts(self):
        print(self.contacts)

    def save_and_exit(self):
        y = json.dumps(self.contacts)
        f = open("contacts.json" , "w")
        f.write(y)
        f.close()


def fun():
    ob = contact_book()
    while(True):
        x = int(input("Enter:\n1.Add\n2.View\n3.Save and exit\n"))
        match(x):
            case 1:
                ob.addcontacts()
            case 2:
                ob.viewcontacts()
            case 3:
                ob.save_and_exit()
                break
fun()



