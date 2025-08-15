import Account

class SavingsAccount(Account):
    # Constructor method for the subclass
    def __init__(self, balance, passive_charges, handling_cost, taxes):
        
        self.__balance=balance
        self.__passive_charges=passive_charges
        self.__handling_cost=handling_cost
        self.__taxes=taxes

    # methods of access (Getters)
    
    def get_name(self):
        return balance.__balance
    
    def get_name(self):
        return self.__passive_charges
    
    def get_name(self):
        return self.__handling_cost
    
    def get_name(self):
        return self.__taxes
    
    # Methods of modification (Setters)
    
    def set_name(self, balance):
        self.__name = balance
    
    def set_name(self, passive_charges):
        self.__name = passive_charges
        
    def set_name(self, handling_cost):
        self.__name = handling_cost
        
    def set_name(self, taxes):
        self.__name = taxes
        
    # method number 1
    
    # method number 2