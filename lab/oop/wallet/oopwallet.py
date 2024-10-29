class Wallet:
    def __init__(self, name, amount):
        self.name = name
        self.balance = amount

    def check(self):
        print(f"ยอดเงินในบัญชี {self.name}: {self.balance} THB")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"ฝากเงินจำนวน: {amount} THB เข้าบัญชี {self.name}")
        else:
            print("ไม่มียอดเงินที่ฝากเข้ามา!")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"ยอดเงินที่ถอน: {amount} THB จากบัญชี {self.name}")
        else:
            print("ไม่มียอดเงินที่ถอน!")


# ทดสอบระบบกระเป๋าเงิน
wallet1 = Wallet("กระเป๋า 1", 1000)
wallet2 = Wallet("กระเป๋า 2", 2000)

wallet1.check()
wallet2.check()

wallet1.deposit(500)
wallet1.check()

wallet2.withdraw(500)
wallet2.check()
