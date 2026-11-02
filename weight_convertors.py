1keep_going = "yes"

while keep_going == "yes":
    weight_kg = float(input("Enter weight in kg: "))
    weight_lbs = weight_kg * 2.205
    print(f"{weight_kg} kg is equal to {round(weight_lbs, 2)} lbs")
    
    keep_going = input("Do you want to convert another weight? (yes/no): ").lower()

print("Goodbye!")
