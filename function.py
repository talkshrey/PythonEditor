#function definition
def multi(a,b):
	print("your function multiplies two numbers given by you:")
	return a*b

def mod(x,y):
	print("returns remainder of 2 numbers: ")
	return x%y

multi(78,43)
print(mod(100,3))

def nature():
	"""
	Function docstring
	-------------------
	returns the type of value the user has entered
	"""
	a = type(input("enter anything:\t"))
	return a

print("the type of value you entered is: ",nature())

def double_multi(x,y):
	prod_1 = multi(x,y)
	return prod_1
	prod_2 = multi(x,prod_1)
	return  prod_2

print(double_multi(4,6))
