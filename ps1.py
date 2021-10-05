# problem 2 part 1

# creating function to predict bill's 10 year wealth

Bill_interest = 0.05

Bill_principle = 1000


def Bill_function(principle, interest):
    total = principle * (1 + interest/1) ** 10
    print("Bill's total wealth is $", round(total, 2))


Bill_function(Bill_principle, Bill_interest)

# Problem 2 part 2

# creating function to predict doubling of Bill's Money

# using rule of 70 for doubling


def Bill_double(interest):
    years = 70 / (interest * 100)
    print("It takes", round(years, 2), " years to double Bill's money.")


Bill_double(Bill_interest)

# problem 2 part 3

Jack_principle = 5000

Jack_interest = .20

# finding out if double

print(70 / (Jack_interest * 100) >= 2 * Jack_principle)
