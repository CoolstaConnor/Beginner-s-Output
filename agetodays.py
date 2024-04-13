years = int(input("Enter your age in years:"))
print("You are", years * 365, "days old.")
if years >= 100:
    print("You have reached 100 years old!")
    exit()
hundred = (100 - years)* 365
print("You will be 100 in", hundred, "days!")