def calculate_vat(food_cost, tax_rate):
    return food_cost * tax_rate


def calculate_total_bill(food_cost, vat_amount, tip_percentage):
    total_cost = food_cost + vat_amount + tip_percentage
    return round(total_cost)


def calculate_change(paid_amount, total_amount):
    change = int(paid_amount - total_amount)  # ทำให้ change เป็น int
    bills = [500, 100, 50, 20, 10, 5, 1]
    change_distribution = {}

    for bill in bills:
        count = change // bill
        if count > 0:
            change_distribution[bill] = count
            change -= bill * count

    return (
        change_distribution,
        paid_amount - total_amount,
    )  # return ค่าเดิมเพื่อแสดงผลทศนิยมใน output


def main():
    tax_rate = 0.07
    food_cost = float(input("Enter food cost: "))
    tip_percentage = float(input("Enter tip: "))

    vat_amount = calculate_vat(food_cost, tax_rate)
    total_amount = calculate_total_bill(food_cost, vat_amount, tip_percentage)

    print(
        f"Food cost with VAT (7%) is {int(food_cost + vat_amount)} baht."
    )  # แสดงผลเป็น int
    print(f"Total cost is {total_amount} baht.")  # แสดงผลเป็น int

    paid_amount = float(input("Enter money to pay: "))

    if paid_amount < total_amount:
        print("The amount paid is not enough.")
    else:
        change_distribution, total_change = calculate_change(paid_amount, total_amount)
        print("Change are:")
        for bill in [500, 100, 50, 20, 10, 5, 1]:
            count = change_distribution.get(bill, 0)
            print(f"\t{bill} baht: {count:.1f}")
        print(f"\tTotal is {total_change:.1f}")  # แสดงผลเป็นทศนิยม 1 ตำแหน่ง


if __name__ == "__main__":
    print("\n__________________ 2.10  ______________\n")
    main()
    print("\n____________________________________\n")
