class Account:
    
    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.no = account_number
        self.balance = initial_amount
        self.count=0
        
    def __iadd__(self,amount):
        self.balance += amount
        self.count+=1
        return self
    
    def __isub__(self,amount):
        self.balance -= amount
        self.count+=1
        return self
    
    def __str__(self):
        s = '%s, %s, balance: %g, total number of transactions: %g' %(self.name, self.no, self.balance, self.count)
        return s
    
    def __repr__(self):
        return "Account(name=%s, account_number=%s, initial_amount=%g)" %(self.name, self.no, self.balance)
        

def test_Account():
    name="John Doe"
    num="12345"
    money=20000
    a = Account(name,num,money)
    tol=1e-14
    diff=abs(money-a.balance)
    success=( diff<tol and name==a.name and num==a.no)
    assert success, "There's a bug in __init__"
    
    a+=(1000)
    diff=abs((money+1000)-a.balance)
    success=diff<tol and a.count==1
    assert success, "There's a bug in deposit"
    
    a-=(2000)
    diff=abs((money-1000)-a.balance)
    success=diff<tol and a.count==2
    assert success, "There's a bug in withdraw"
    
    print (a)
    a

test_Account()

