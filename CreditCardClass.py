# This is CreditCard class  ### this class does not include error catching like invalid input's by the user
# this is not robust 
class CreditCard:        
    def __init__(self,name,bank_name,account_no,balance,limit): # all initial data required to make credit card class 
        self._name=name
        self._bank=bank_name
        self._account_no=account_no
        self._balance=balance
        self._limit=limit
    def add_money(self,money): # this add money in your card and used to add money you got
        self._balance+=money
        return self._balance
    def get_customer(self): # this method return name 
        return self._name
    def get_bank(self): # this method returns the bank name 
        return self._bank
    def get_account(self): # this method returns account no
        return self._account_no
    def make_payment(self,amount): # this method make payment
        self._balance -= amount
        
        return self._balance
    def get_balance(self): # this method returns balance 
        return self._balance
    def get_limit(self): # this is not of any use because i am limitless
        return self._limit
    def charge(self,price): # this chage rs 5 in every transcation
        self._balance-=5
        return self._balance
    def transfer(self,to_whom,price): # this transfer money to the particular instance of this class but there is an unconvience it does not raise a exception when
        # money is transfered to invalid instance of class i don't know why but we will try to fix it up
       
        if self._balance-price>0:  # this line checks that there must be sufficient amount as balance 
            try:
                self._balance-=price # substract the price from balance 
                self.charge(price)  # this charge unit 5 as transcation fee ( bussiness comes in play )
                to_whom.add_money(price) # this will add money to the other instance of this class
                return "transfered",price,'amount_left',self._balance # return transfered money and balance left 
            except Exception as e: # ?
                raise "INVALID CREDIT CARD NAME"
        else:
            return " WORK more HARD you don't have enough money " # if insufficent money as balance 
class PredatoryCreditCard(CreditCard): # this is the child class which i made after watching from book
    
    def __init__(self,name,bank_name,account_no,balance,limit,apr): # here we take all the parameter required by the parent class and plus the parameter of this class
        super().__init__(name,bank_name,account_no,balance,limit) # here we initialize all the parameter of parent class
        self._apr = apr # you know what it is for 
        
    def charge(sefl,price):
        succes= super().charge(price)
        if not succes:
            self.balance+=5
            return succes
        
    def process_month(self):
        if self._balance> 0:
            monthly_factor = pow(1+self._apr,1/12)
            self._balance *= monthly_factor
            return self._balance
        
class Third(CreditCard):  # This class is made by me ok (CreditCard) shows that take all property of Credit Card Class
    def __init__(self,name,bank_name,account_no,balance,limit): # here we takes all required parameter by parent class
        super().__init__(name,bank_name,account_no,balance,limit) # here we intialize them and if we have parameter for this class we initialize them here
    def zero(self): # from here we add extra modules to this class 
        self._balance=0
        return self._balance
    

                
        
        
        
        
        
    
