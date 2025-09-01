# This program calculates a meal total and an alarm time based on user input.

# Part 1: Restaurant Bill Calculator

# Prompt the user for the charge for the food and convert to a number.
food_charge = float(input("Enter the charge for the food: $"))

# Calculate the tip (18%), sales tax (7%), and total.
tip_rate = 0.18
tax_rate = 0.07

tip_amount = food_charge * tip_rate
tax_amount = food_charge * tax_rate
total_price = food_charge + tip_amount + tax_amount

# Display the results.
print("\n--- Meal Summary ---")
print(f"Tip (18%): ${tip_amount:.2f}")
print(f"Sales Tax (7%): ${tax_amount:.2f}")
print(f"Total Price: ${total_price:.2f}")
print("--------------------")

# --- End of Part 1 ---

# Part 2: 24-Hour Alarm Clock

# Add a separator for clarity.
print("\n--- Part 2: 24-Hour Alarm Clock ---")

# Prompt the user for the current time and the number of hours to wait, and convert to integers.
current_time = int(input("Enter the current time (in hours, 0-23): "))
hours_to_wait = int(input("Enter the number of hours to wait for the alarm: "))

# Calculate the time the alarm will go off using the modulo operator for the 24-hour cycle.
alarm_time = (current_time + hours_to_wait) % 24

# Display the result.
print(f"\nThe alarm will go off at {alarm_time}:00 on the 24-hour clock.")

# --- End of Part 2 ---