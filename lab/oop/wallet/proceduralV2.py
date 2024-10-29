def create(name, amount):
    return {"name": name, "money": amount}


def check(wallet):
    print(f"ยอดเงินในบัญชี {wallet['name']}: {wallet['money']} THB")


def deposit(wallet, amount):
    if amount > 0:
        wallet["money"] += amount
        print(f"ฝากเงินจำนวน: {amount} THB เข้าบัญชี {wallet['name']}")
    else:
        print("ไม่มียอดเงินที่ฝากเข้ามา!")


def withdraw(wallet, amount):
    if 0 < amount <= wallet["money"]:
        wallet["money"] -= amount
        print(f"ยอดเงินที่ถอน: {amount} THB จากบัญชี {wallet['name']}")
    else:
        print("ไม่มียอดเงินที่ถอน!")


wallet1 = create("กระเป๋า 1", 1000)
wallet2 = create("กระเป๋า 2", 2000)

check(wallet1)
check(wallet2)

deposit(wallet1, 500)
check(wallet1)

withdraw(wallet2, 500)
check(wallet2)
