# list
myList = ["shrey", "hardik", "adi", "harsh", "shubham", "shubh", "anubhav"]
print(len(myList))
myList.sort()
print(myList)
myList.remove("anubhav")
print(myList)
myList.insert(4, "krish")
print(myList)
print(myList[3])
print(slice(myList[0:2]))
print(type(myList))
print(dict(enumerate(myList)))

# tuples
"""tuple is not changeable like a list
   always use round bracket """
myTuple = ("shrey", "asmi", "bhivash", "mona")
print(myTuple)
print(slice(myTuple[1:3]))

# set
"""unordered unindexed with curly brackets """
mySet = {"NIT", "IIT", "MU", "IIIT"}
# order may change everytime you print a set
print(mySet)
mySet.add("BITS")
mySet.remove("MU")
print(mySet)

# dictionary
"""unordered but changeable and indexed
   you assign a value to each element """
myDict = {"rushikesh": 1, "krish": 2, "kaushal": 3, "shrey": 4}
print(myDict)
print(list(enumerate(myDict)))
print(myDict.values())
print(myDict.keys())
print(myDict.get('shrey'))
   
string = "12345"
n = len(string)
print(n)

""" enumerate function creates list or dictionary based 
    on user's choice ; the user needs to specify whether to use a list 
    class or an dict class"""

a = list(range(1, 10))
# value of list a is stored in b
b = a
# value of list a is explicitly sotred in c
c = a.copy()
a.insert(3,18)
print(a)
print(b)
print(c)

