# THIS IS A TIP CALCULATOR APP 🤑🤑

food_amount = float(input("Enter your Food Amount: $"))
food_percentage = float(input("Enter Tip Percentage (e.g., 15 for 15%): ")) / 100
tip_amount = food_amount * food_percentage

# LET'S MAKE THE TOTAL VALUE 💵 💵 💵 💵 💵 💵
total = food_amount + tip_amount

# LET'S PRINT THOSE THINGS [̲̅$̲̅(̲̅ιοο̲̅)̲̅$̲̅]
print("--------------------------------------------------")
print(f"🍗Food Amount: ${food_amount:.2f}")
print(f"📌Tip Amount: ${tip_amount:.2f}")
print("\n")
print(f"💸Total Amount: ${total:.2f}")
print("--------------------------------------------------")


