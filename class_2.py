#creating class
class Student :
    college_name = "IIIT surat\t"
    course = "B.tech\t"

    # defining instance atrributes, this is called method function
    def details(self, name, age, marks):
        print("student name: ", name)
        print("student age: ", age)
        print("marks out of 100: ", marks, "\n")

#creating objects
student1 = Student()
student2 = Student()

#calling class attributes
print(student1.college_name,student1.course)

#calling instance attributes
student1.details("hardik","18","95")
student2.details("shrey","18","98")