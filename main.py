def check_age():
    valid = False
    while not valid:
        try:
            response = int(input(question))
            if response <= LOW or response >= HIGH:
                print("Please enter a valid age")
                valid = False
            else:
                valid = True
                return response
        except ValueError:
            print("Please enter a valid age")

#jack is here
# Variables
name = input("What is your name? ")
nz_resident = input("Are you a New Zealand resident? ")
question = "What is your age? "
LOW = 0
HIGH = 30

age = check_age()

if age >= 18 and nz_resident.lower() == "yes":
    print("You are eligible to vote {}".format(name))

else:
    print("You are not eligible to vote {}".format(name))
