money = 100


def check():
    print(f"ยอดเงินในบัญชี: {money} ฿")


def deposit(amount):
    global money
    if amount > 0:
        money += amount
        print(f"ฝากเงินจำนวน: {amount} ฿")
    else:
        print("ไม่มียอดเงินที่ฝากเข้ามา")


def withdraw(amount):
    global money
    if 0 < amount <= money:
        money -= amount
        print(f"ยอดเงินที่ถอน: {amount} THB")
    else:
        print("ไม่มียอดเงินที่ถอน")


check()
deposit(500)
check()
withdraw(300)
check()
withdraw(500)
check()
