def calculate_vat(food_cost, tax_rate):
    return food_cost * tax_rate


def calculate_total_bill(food_cost, vat_amount, tip_percentage):
    total_cost = food_cost + vat_amount + tip_percentage
    return round(total_cost)


def main():
    tax_rate = 0.07
    food_cost = float(input("Enter food cost: "))
    tip_percentage = float(input("Enter tip percentage: "))

    vat_amount = calculate_vat(food_cost, tax_rate)
    total_amount = calculate_total_bill(food_cost, vat_amount, tip_percentage)

    print(f"Food cost with VAT (7%) is {food_cost + vat_amount:.2f} baht.")
    print(f"Total cost is {total_amount} baht.")


if __name__ == "__main__":
    print("\n______________ 2.8   ______________\n")
    main()
    print("\n____________________________________\n")
