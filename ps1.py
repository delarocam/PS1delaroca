"""This document is to track and calculate interest for customers of a bank.
 We also wat to practice converting data into various data structures"""

# problem 2.1

# creating function to predict bill's 10 year wealth

BILL_INTEREST = 0.05

BILL_PRINCIPLE = 1000


def bill_function(principle, interest):
    """This function is to calculate bills interest in ten years, given any input
of principle and interest"""
    total = principle * (1 + interest/1) ** 10
    print("Bill's total wealth is $", round(total, 2))


bill_function(BILL_PRINCIPLE, BILL_INTEREST)

# Problem 2.2

# creating function to predict doubling of Bill's Money

# using rule of 70 for doubling


def bill_double(interest):
    """this function is to calcuate the doubling time for bill's money given any
interest amount"""
    years = 70 / (interest * 100)
    print("It takes", round(years, 2), " years to double Bill's money.")


bill_double(BILL_INTEREST)

# problem 2.3

JACK_PRINCIPLE = 5000

JACK_INTEREST = .20

# finding out if double

print(JACK_PRINCIPLE * (1 + JACK_INTEREST/1) ** 6 >= 2 * JACK_PRINCIPLE)

# 2.4: creating a list

accounts_list = ["Bill", 1000, "Jack", 5000, "Amy", 6700, "Cindy",
                 5699, "Harry", 6700]

print(accounts_list)

# 2.5 creating dictonary out of former information using zip object

zipobj = zip(accounts_list[::2], accounts_list[1::2])

Accounts = dict(zipobj)

print(Accounts)

# 2.6 creating list of tuples

tuple_accounts = list(Accounts.items())

print(tuple_accounts)

# explanation of list,tuple, dictionary
# list = a sequence of elements of any type, either characters,
# float, numeric or boolean.
# dictionary = is like a list but contains a key and value, which maps the
# relationship between different elements
# tuple = like lists and dictionaries, store elements. Unlike the former, they
# are immutable, meaning elements cannot be deleted or added after creation.

# running pylint
