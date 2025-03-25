def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price * ( discount_percent / 100)
    else:
        return price

def main():
    price = int(input("Enter Amount: "))
    discount_percent = int(input("Enter Discount: "))
    final_price = calculate_discount(price, discount_percent)
    print(f"The final price after applying the discount is: {final_price}")

if __name__ == "__main__":
    main().
