# Gym Membership System

def calculate_discount(age, married):
    
    if married == "yes":
        return 30
    
    elif 18 <= age <= 45:
        return 35.5
    
    elif age < 18:
        return 15
    
    else:
        return 25


print("\n" + "="*35)
print("🏋️ Welcome to Gym Membership 💪")
print("="*35)

# Input
age = int(input("Enter your age: "))

# Negative age check
if age < 0:
    print("❌ Invalid input! Age cannot be negative.")
else:
    married = input("Are you married? (yes/no): ").lower()

    # Membership price (example)
    price = 1000  

    # Get discount
    discount = calculate_discount(age, married)

    # Final price
    final_price = price - (price * discount / 100)

    # Output
    print("\n" + "-"*35)
    print(f"🎉 Discount Applied: {discount}%")
    print(f"💰 Final Price: ₹{final_price}")
    print("-"*35)