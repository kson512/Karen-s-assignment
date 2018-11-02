# This was adapted from https://www.pythonforbeginners.com/
import random
print("Welcome to Karen's random number generator! You will receive two random numbers.\n")
min = 1
max = 100
# Player will receive a random number from 1 to 100.
ran_num = "yes"
while(ran_num == "yes"):
    print("Generating your random numbers...\n")
    print("This will take just a moment...\n")
    print("And your random numbers are...\n")
    print random.randint(min, max)
    print("and")
    print random.randint(min, max)
    print(" ")
    # Used a blank space to make it look cleaner
    ran_num = raw_input("Would you like more numbers?\n")
    if(ran_num == "no"):
        print("Alright.....")
print("Good bye.....:(")