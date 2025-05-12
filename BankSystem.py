import csv

# account: account number (8 digit), name, balance
class BankAccount:
    def __init__(self, account_id, name, balance):
        self.account_id = account_id
        self.name = name
        self.balance = balance

    def withdraw(self, money):
        if money <= 0:
            print('amount cannot be negative')
            return False
        if self.balance >= money:
            self.balance -= money
            return True
        else:
            print('insufficient balance')
            return False

    def deposit(self, money):
        if money <= 0:
            print('amount cannot be negative')
            return False
        self.balance += money
        return True



class BankSys:
    def __init__(self):
        self.accounts = {}   # dict {account_id: BankAccount}
        self.nextID = 100000

    def transfer(self, source_id, target_id, money):     # money transfer
        if source_id == target_id:
            print('same account')
            return False
        source = self.accounts.get(source_id)
        target = self.accounts.get(target_id)
        if source is None or target is None:
            print('invalid account number')
            return False
        if source.withdraw(money):
            target.deposit(money)
            return True
        return False

    def new_account(self, name, init_balance=0):  # create new account
        if init_balance < 0:
            print('balance must be positive')
            return False
        id = self.nextID
        self.nextID += 1
        account = BankAccount(id, name, init_balance)
        self.accounts[id] = account
        # print(f'success, account ID is {id}, balance is {init_balance}')
        return id

    def deposit(self, source_id, money):  # deposit money
        source = self.accounts.get(source_id)
        if source is None:
            print('invalid account number')
            return False
        if source.deposit(money):
            return True
        return False

    def withdraw(self, source_id, money):  # withdraw money
        source = self.accounts.get(source_id)
        if source is None:
            print('invalid account number')
            return False
        if source.withdraw(money):
            return True
        return False

    def load_from_csv(self, dir):  # load state from csv file, this op will clear current state
        try:
            with open(dir, 'r', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                self.accounts = {}
                for row in reader:
                    try:
                        account_id = int(row[0])
                        name = row[1]
                        balance = float(row[2])
                    except ValueError:
                        print("Invalid values")
                        continue
                    if balance < 0:
                        print(f"{account_id}:balance cannot be negative")
                        continue
                    self.accounts[account_id] = BankAccount(account_id, name, balance)
            self.nextID = max(self.accounts.keys()) + 1
            return True
        except FileNotFoundError:
            print('file not found')
            return False

    def save_to_csv(self, dir):      # save state from csv file
        with open(dir, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            for row in self.accounts.values():
                writer.writerow([row.account_id, row.name, row.balance])
        return True