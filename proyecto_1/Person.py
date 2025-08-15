class Person:

    # Constructor for the Person class 
    def __init__(self, name="", last_name="", document_id="", document_type="", birthdate="", email="", phone_number="", address="", city="", country="", postal_code=""):
        self.__name = name
        self.__last_name = last_name
        self.__document_id = document_id
        self.__document_type = document_type
        self.__birthdate = birthdate
        self.__email = email
        self.__phone_number = phone_number
        self.__address = address
        self.__city = city
        self.__country = country
        self.__postal_code = postal_code
    
    # Getters for the Person class
    def get_name(self):
        return self.__name
    
    def get_last_name(self):
        return self.__last_name
    
    def get_document_id(self):
        return self.__document_id
    
    def get_document_type(self):
        return self.__document_type
    
    def get_birthdate(self):
        return self.__birthdate
    
    def get_email(self):
        return self.__email
    
    def get_phone_number(self):
        return self.__phone_number
    
    def get_address(self):
        return self.__address
    
    def get_city(self):
        return self.__city
    
    def get_country(self):
        return self.__country
    
    def get_postal_code(self):
        return self.__postal_code
    
    # Setters for the Person class
    def set_name(self, name):
        self.__name = name

    def set_last_name(self, last_name):
        self.__last_name = last_name
    
    def set_document_id(self, document_id):
        self.__document_id = document_id
    
    def set_document_type(self, document_type):
        self.__document_type = document_type
    
    def set_birthdate(self, birthdate):
        self.__birthdate = birthdate
    
    def set_email(self, email):
        self.__email = email

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number
    
    def set_address(self, address):
        self.__address = address

    def set_city(self, city):
        self.__city = city

    def set_country(self, country):
        self.__country = country

    def set_postal_code(self, postal_code):
        self.__postal_code = postal_code
    


    # This method requests personal information from the user
    def request_personal_info(self, name="", last_name="", document_id="", document_type="", birthdate="", email="", phone_number="", address="", city="", country="", postal_code=""):
        
        print("\nPlease enter your personal information:\n")
        name = input("Enter your Name: ")
        last_name = input("Enter your Last Name: ")
        document_id = input("Enter your Document ID: ")
        document_id = input("Enter your Document Type: ")
        birthdate = input("Enter your Birthdate (YYYY-MM-DD): ")
        email = input("Enter your Email: ")
        phone_number = input("Enter your Phone Number: ")
        address = input("Enter your Address: ")
        city = input("Enter your City: ")
        country =input("Enter your Country: ")
        postal_code = input("Enter your Postal Code: ")

        self.set_name(name)
        self.set_last_name(last_name)
        self.set_document_id(document_id)
        self.set_document_type(document_type)
        self.set_birthdate(birthdate)
        self.set_email(email)
        self.set_phone_number(phone_number)
        self.set_address(address)
        self.set_city(city)
        self.set_country(country)
        self.set_postal_code(postal_code)

    # This method displays the personal information of the person
    def show_personal_info(self):
        print(f"Name: {self.get_name()}")
        print(f"Last Name: {self.get_last_name()}")
        print(f"Document ID: {self.get_document_id()}")
        print(f"Document Type: {self.get_document_type()}")
        print(f"Birthdate: {self.get_birthdate()}")
        print(f"Email: {self.get_email()}")
        print(f"Phone Number: {self.get_phone_number()}")
        print(f"Address: {self.get_address()}")
        print(f"City: {self.get_city()}")
        print(f"Country: {self.get_country()}")
        print(f"Postal Code: {self.get_postal_code()}")
        


# This is the main program loop that interacts with the user
while True:
    print("Welcome to the Personal Information System")
    print("Menu:")
    print("1. Enter Personal Information")
    print("2. Show Personal Information")
    print("3. Exit")
    choice = input("Please select an option: ")
    if choice == "1":
        try:
            person1 = Person()
            person1.request_personal_info()
        except Exception as e:
            print(f"An error occurred: {e}")
    elif choice == "2":
        try:
            person1.show_personal_info()
        except Exception as e:
            print(f"An error occurred: {e}")
    elif choice == "3":
        print("Exiting the system. Goodbye!")
        break
    

