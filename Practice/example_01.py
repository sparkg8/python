
class Person:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


class Customer(Person):

    def __init__(self, firstname, lastname, account_number, balance=0):
        Person.__init__(self, firstname, lastname)
        self.account_number = account_number
        self.balance = balance

    """solution"""
    # This method will show the texts
    def __str__(self):
        return f'Client: {self.firstname} {self.lastname}\nAccount Balance: {self.account_number} -> ${self.balance}'


    def deposits(self, deposit):
        self.balance = self.balance + deposit
        print(f'Balance after deposit: ${self.balance}')
    
    def withdrawal(self, amount):
        # first check if the balance is enough to give the amount to the clien
        if self.balance >= amount:
            self.balance -= amount
            print(f'Balance after withdraw: ${self.balance}')
        
        else:
            print(f'Error Insuficient money!...try another amount {self.balance}')



"""Create customer"""
def create_customer():
    c_name = input("Enter your name: ")
    c_lastname = input("Enter your last name: ")
    c_acount_id = input("Enter your acount ID: ")
    print("------------------------------------------------------")
    client1 = Customer(c_name, c_lastname, c_acount_id)

    return client1

"""start program"""
def start():
    my_customer = create_customer()
    print(my_customer)
    option = 0

    while option != 'E':
        print("Choose: Deposit (D), Withdraw (W), or Exit(E)")
        option = input()

        if option == 'D':
            dep_amount = int(input("Deposit amount: $"))
            my_customer.deposits(dep_amount)
        elif option == 'W':
            wit_amount = int(input("Withdrawa amount: $"))
            my_customer.withdrawal(wit_amount)

        print(my_customer)
        print("------------------------------------------------------")

    print(f'See you soon...{my_customer.firstname}\n')

# call our start function
start()




