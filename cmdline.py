import argparse

# creating an object using ArgumentParser method
parser = argparse.ArgumentParser()

# creating command line function with the name number
parser.add_argument("--number", type=int, help="Enter a number")

# using the parse_args function
args = parser.parse_args()

# performing the function
num = args.number
print("the required number is: ", num+5)