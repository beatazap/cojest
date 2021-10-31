import random
# https://docs.python.org/3.9/library/decimal.html
# https://docs.python.org/3.9/tutorial/floatingpoint.html 
from decimal import *
getcontext().prec = 4


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
        self.wire_transfers = []
        
    def deposits(self):
        total_deposit = Decimal(0)
        for account_no, account in self.accounts.items():
            total_deposit += account.total_balance
        return total_deposit
    
    def create_account(self, firstname, lastname):
        # tworzymy listę z stałymi wartościami określającymi numer naszego-banku
        account_number = ['10', '5555']
        # generujemy dodatkowe trzy cztero-cyfrowe losowe liczby
        for _ in range(3):
            account_number.append(f"{random.randint(0, 9999):04d}")
        account_number = "-".join(account_number)
        # Tworzymy nową instancję klasy Account, w której przechowujemy
        # potrzebne nam informacje.
        new_account = Account(account_number, firstname, lastname)
        # W celu szybszego wyszukania odpowiedniego obiektu, przechowujemy go w słowniku
        # gdzie kluczem jest numer konta a wartością nasz nowy obiekt klasy Account.
        self.accounts[account_number] = new_account
        return account_number
    
    def list_accounts(self):
        print("Dostępne konta:")
        for account_no in self.accounts:
            print(account_no, ":", self.accounts[account_no])

    # przekazanie pieniędzy na czyjeś konto
    def send_money(self, sender_no, receiver_no, amount):
        sender = self.get_account(sender_no)
        receiver = self.get_account(receiver_no)
        if sender.total_balance >= amount:
            sender_wire = WireTransfer(sender_no, receiver_no, amount)
            sender.total_balance -= Decimal(amount)
            receiver.total_balance += Decimal(amount)
            self.wire_transfers.append(sender_wire)
        else:
            print("Brak środków na koncie.")
   
    # wpłata w okienku
    def deposit_money(self, receiver_no, amount):
        receiver = self.get_account(receiver_no)
        w = WireTransfer("depozyt", receiver_no, amount)
        # aktualizujemy historię transferów (historię dla konta odbiorcy)
        receiver.wire_transfers.append(w)
        receiver.total_balance += Decimal(amount)
        # aktualizujemy historię transferów (historię w banku)
        self.wire_transfers.append(w)
    
    # metoda pozwalająca nam pobrać obiekt z słownika po numerze konta
    def get_account(self, account_no):
        return self.accounts[account_no]
    
    def __str__(self):
        return f"{self.name} Bank Polski"
                                     
    
class Account:
    """Klasa Account do przechowywania informacji o koncie."""
    def __init__(self, number, firstname, lastname):
        self.number = number
        self.firstname = firstname
        self.lastname = lastname
        self.total_balance = Decimal(0)
        self.wire_transfers = []

    def show_history(self):
        print(f"Historia dla konta o numerze {self.number}:")
        for wire in self.wire_transfers:
            print(f"z *{wire.from_number}* do *{wire.to_number}* na kwotę {wire.amount:.2f} PLN")
        print(f"Saldo: ${self.total_balance:.2f}")
            
    def __str__(self):
        return f"'{self.firstname} {self.lastname}' konto z saldem: {self.total_balance:.2f} PLN"

    
class WireTransfer:
    """Klasa WireTransfer do przechowywania informacji o przelewach."""
    def __init__(self, from_number, to_number, amount):
        self.from_number = from_number
        self.to_number = to_number
        self.amount = Decimal(amount)
        
    def __str__(self):
        return f"z *{self.from_number}* do *{self.to_number}* na kwotę {self.amount:.2f} PLN"
                                     

if __name__ == "__main__":
    bank = Bank("Narodowy")
    print(f"Witamy w {bank}")                            
    michals_account_no = bank.create_account('Michał', 'Michał')
    mariusz_account_no = bank.create_account('Mariusz', 'Mariusz')
    karolina_account_no = bank.create_account('Karolina', 'Karolina')
    print("-" * 60)
    print(f"Wszystkie pieniądze w banku: {bank.deposits():.2f} PLN")
    print("-" * 60)
    bank.list_accounts()
    monika_account_no = bank.create_account('Monika', 'Monika')
    print("-" * 60)
    bank.list_accounts()
    print("-" * 60)
    michals_account = bank.get_account(michals_account_no)
    bank.deposit_money(michals_account_no, 500.00)
    bank.deposit_money(michals_account_no, 125.70)
    bank.deposit_money(monika_account_no, 560.70)
    print(f"Wszystkie pieniądze w  banku: {bank.deposits():.2f} PLN")
    print("-" * 60)
    bank.send_money(michals_account_no, mariusz_account_no, 23.23)
    bank.list_accounts()
    print("-" * 60)
    bank.send_money(michals_account_no, karolina_account_no, 323.23)
    mariusz_account = bank.get_account(mariusz_account_no)
    mariusz_account.show_history()
    print("-" * 60)
    michals_account.show_history()
    print("-" * 60)
    print(f"Wszystkie pieniądze w banku: {bank.deposits():.2f} PLN")
    print("-" * 60)
    bank.list_accounts()
    print("-" * 60)
    print(f"Wszystkie pieniądze w banku: {bank.deposits():.2f} PLN")
    print("-" * 60)
    
