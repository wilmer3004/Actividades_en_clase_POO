class Bank:

    #constructor class
    def __init__(self,name, direction, city, nit, country, email, postal_code):
        self.__name = name
        self.__direction = direction
        self.__city = city
        self.__nit = nit
        self.__country = country
        self.__email = email
        self.__postal_code = postal_code

    #getters for the person class

        def get_name(self):
            return self.__name
        
        def get_direction(self):
            return self.__direction
        
        def get_city(self):
            return self.__city
        
        def get_nit(self):
            return self.__nit
        
        def get_country(self):
            return self.__country
        
        def get_email(self):
            return self.__email
        
        def get_postal_code(self):
            return self.__postal_code
    
    # set
        

        def set_name(self, name):
            self.__name = name

        def set_direction(self, direction):
            self.__direction = direction    
        
        def set_city(self, city):
            self.__city = city  

        def set_nit(self, nit):
            self.__nit = nit

        def set_country(self, country):
            self.__country = country

        def set_email(self, email):
            self.__email = email

        def set_postal_code(self, postal_code):
            self.__postal_code = postal_code


        
                

        
        
