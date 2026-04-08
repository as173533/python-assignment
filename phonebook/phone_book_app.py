class PhoneBook:
    phone_directory =[]
    def __init__(self,name, phone_number):
        self.name = name
        self.phone = phone_number
        PhoneBook.phone_directory.append(self)

    def show_contact(self):
        print(f"Name: {self.name}, Contact Number: {self.phone}")

    @classmethod
    def show_all_contact(cls):
        if(len(cls.phone_directory)>0):
            print("All contacts are showing from the directory")
            for contact in cls.phone_directory:
                contact.show_contact()
        else:
            print("No Contacts found in directory.")

    @classmethod
    def search_contact(cls,name):
        for contact in cls.phone_directory:
            if contact.name.lower() == name.lower():
                return contact.phone

        return f"No contacts found in {name}"

    @staticmethod
    def validate_phone_number(phone_number):
        if len(phone_number)==10 and phone_number.isdigit():
            return True
        else:
            return False
n_contact = int(input("How many contacts do you want? "))

for i in range(n_contact):
    name = input("Enter the name: ")
    phone_number = input("Enter the phone number: ")
    if PhoneBook.validate_phone_number(phone_number):
        PhoneBook(name,phone_number)
    else:
        print(f"Invalid phone number for {name} entered.")
# c2 = PhoneBook("Vivek", 1234567890)
# c3 = PhoneBook("Carol", 6549871230)
# c1.show_contact()

PhoneBook.show_all_contact()
# print(PhoneBook.search_contact("carol"))