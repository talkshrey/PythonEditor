#creating a class
class Student :
    #class attributes
    college_name = "DJ sanghvi\t"
    course = "B.tech\t"

    #creating constructor
    def __init__(self,name,field):
        self._name = name
        self._field = field

#defining constructor while creating object of class Student
student1 = Student("shrey","computer science")
student2 = Student("hardik","IT")

#calling class attributes
print(student1.college_name,student1.course)

#calling constructor
print(student1._name,student1._field,student1.college_name)
print(student2._name,student2._field,student2.college_name)
