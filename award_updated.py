def must_use_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if not isinstance(value, float):
                raise ValueError("Invalid input. Please enter a numeric value.")
            return value
        except ValueError:
            print("Invalid input. Provide a numeric value.")
            

swim_time = must_use_number("Enter minutes swimming: ")
bike_time = must_use_number("Enter minutes cycling : ")
run_time = must_use_number("Enter minutes running: ")

total_time_marathon = swim_time + bike_time + run_time

award_ranges = {
    "Provincial Colors": (0, 100),
    "Provincial Half Colors": (101, 105),
    "Provincial Scroll": (106, 110),
    "No": (111, float("inf"))
}

award = None
for category, (min_time, max_time) in award_ranges.items():
    if min_time <= total_time_marathon <= max_time:
        award = category
        break

if award:
    print(f"You qualify for an {award} award. ")
else:
    print("No award recieved.")