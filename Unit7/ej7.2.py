class Account(object):
    
    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.no = account_number
        self.balance = initial_amount
        self.count=0
    
    def deposit(self, amount):
        self.balance += amount
        self.count+=1
        
    def withdraw(self, amount):
        self.balance -= amount
        self.count+=1
        
    def dump(self):
        s = '%s, %s, balance: %g, total number of transactions: %g' %(self.name, self.no, self.balance, self.count)
        print (s)

def test_Account():
    name="John Doe"
    num="12345"
    money=20000
    a = Account(name,num,money)
    tol=1e-14
    diff=abs(money-a.balance)
    success=( diff<tol and name==a.name and num==a.no)
    assert success, "There's a bug in __init__"
    
    a.deposit(1000)
    diff=abs((money+1000)-a.balance)
    success=diff<tol and a.count==1
    assert success, "There's a bug in deposit"
    
    a.withdraw(2000)
    diff=abs((money-1000)-a.balance)
    success=diff<tol and a.count==2
    assert success, "There's a bug in withdraw"

test_Account()
