# --- GLOBAL SCOPE ---
# These limits apply to everyone across the whole airport
MAX_WEIGHT = 23  # Bags cannot weigh more than 23 kg
DANGER_ITEMS = ["fireworks", "gasoline", "explosives"]

def check_baggage(passenger_name, bag_weights, bag_contents):
    # --- LOCAL SCOPE ---
    # These variables only exist inside this function for this specific passenger
    print(f"--- Checking baggage for {passenger_name} ---")
    
    # 1. Using enumerate() to list bags with their weight
    for index, weight in enumerate(bag_weights, start=1):
        print(f"Bag {index} weight: {weight}kg")
    
    # 2. Using all() to check if ALL bags are under the weight limit
    # This creates a True/False list: [True, True, False] if the 3rd bag is too heavy
    all_bags_safe_weight = all(weight <= MAX_WEIGHT for weight in bag_weights)
    
    # 3. Using any() to check if ANY dangerous item is in the bags
    has_danger = any(item in DANGER_ITEMS for item in bag_contents)
    
    # Final Decision Logic
    if all_bags_safe_weight and not has_danger:
        return "PASS: Baggage cleared for flight!"
    else:
        return "FAIL: Baggage rejected! (Check weight limits or prohibited items)"

# --- Running the code ---
passenger_1_decision = check_baggage("Alice", [20, 15, 25], ["clothes", "books", "shoes"])
print(passenger_1_decision) 
# Result will be FAIL because the 3rd bag (25kg) is over the MAX_WEIGHT (23kg).
