class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
        self.history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(f"Deposit: +{amount}")
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.history.append(f"Withdrawal: -{amount}")
            return True
        return False

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Wlasciciel konta: {self.owner}, stan konta: {self.balance}"


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def get_total_balance(self):
        return sum(account.get_balance() for account in self.accounts)

    def __str__(self):
        return f"Bank {self.name}, liczba kont: {len(self.accounts)}"


def main():
    bank = Bank("MEGABANK")
    account1 = BankAccount("Ignacy Kmiecik")
    account2 = BankAccount("Jaromir Limanówka")

    bank.add_account(account1)
    bank.add_account(account2)

    while True:
        print("\nMenu:")
        print("1. Wyświetl stan kont")
        print("2. Wpłac pieniadze")
        print("3. Wypłac pieniadze")
        print("4. Wyświetl stan banku")
        print("5. Wyjście")

        choice = input("Wybierz opcje: ")

        if choice == "1":
            for account in bank.accounts:
                print(account)
        elif choice == "2":
            amount = float(input("Podaj kwotę do wplaty: "))
            account = int(input("Wybierz konto (1 lub 2): "))
            if account == 1:
                account1.deposit(amount)
            elif account == 2:
                account2.deposit(amount)
        elif choice == "3":
            amount = float(input("Podaj kwotę do wyplaty: "))
            account = int(input("Wybierz konto (1 lub 2): "))
            if account == 1:
                account1.withdraw(amount)
            elif account == 2:
                account2.withdraw(amount)
        elif choice == "4":
            print(bank)
        elif choice == "5":
            break
        else:
            print("Niepoprawny wybor!")


if __name__ == "__main__":
    main()