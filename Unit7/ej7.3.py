from datetime import datetime
t=datetime.now()


class AccountP:
    def __init__(self, name, account_number,
                 initial_amount):
        self._name = name
        self._no = account_number
        #self._balance = initial_amount
        self._transactions=[{datetime.now():initial_amount}]
       
    def deposit(self, amount):
        self._transactions.append({datetime.now():amount})
        #self._balance += amount
        
    def withdraw(self, amount):
        self._transactions.append({datetime.now():-amount})
        #self._balance -= amount
        
    def get_balance(self):
        tot= sum([sum(elem.values()) for elem in self._transactions])
        return tot
    
    def dump(self):
        print("      time            ammount    balance")
        b=0
        for elem in self._transactions:
            b+=sum(elem.values())            
            print ("%-20s %7g  %10g"  %(list(elem.keys())[0].isoformat(sep=' ', timespec='seconds'),  list(elem.values())[0], b ))
    
        
a=AccountP("John Doe","12058741",20000)
a.deposit(1000)
a.deposit(1000)
a.deposit(1000)
a.withdraw(3500)
a.dump()
