productNames = []    
productPrices = []    
productQuantities = []

def add_item():
    print("\nEnter product details:")
    
    name = input("Product name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))
    
    productNames.append(name)
    productPrices.append(price)
    productQuantities.append(quantity)
    
    print("Item added successfully!")

def print_receipt():

    print("\n====================================")
    print("           STORE RECEIPT            ")
    print("====================================")
    
    subtotal = 0
    
    print("\nItems Purchased:")
    print("----------------------------------")
    
    for i in range(len(productNames)):
    
        itemTotal = productPrices[i] * productQuantities[i]
        subtotal += itemTotal
        
        print(f"{productNames[i]:<20} x {productQuantities[i]}  #{itemTotal:.2f}")
    
    vat = subtotal * 0.075
    
    discount = 0
    if subtotal > 10000:
        discount = subtotal * 0.05
    
    final_total = subtotal + vat - discount
    
    print("\n----------------------------------")
    print(f"Subtotal:         #{subtotal:.2f}")
    print(f"VAT (7.5%):       #{vat:.2f}")
    print(f"Discount:         #{discount:.2f}")
    print(f"Total:            #{final_total:.2f}")
    print("====================================")
    print("Thank you for shopping with us!")

def main():
    while True:
    
        print("\nStore Checkout System")
        print("1. Add new item")
        print("2. Print receipt")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")
        
        if choice == "1":
            add_item()
        elif choice == "2":
            print_receipt()
        elif choice == "3":
            print("Thank you for using our system!")
            break
        else:
            print("Please choose a valid option!")

if __name__ == "__main__":
    main()
