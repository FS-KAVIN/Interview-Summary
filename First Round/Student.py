class student:
    def __init__(self,name,age,dob):
        self.name = name
        self.age = age
        self.dob = dob


if __name__ == '__main__':
    student1 = student("name1","age1","dob1")
    student2 = student("name2", "age2", "dob2")
    student3 = student("name3", "age3", "dob3")

    print(student1.name,student1.age,student1.dob)