from dataclasses import dataclass
# dataclass tidies up the code very nicely and
# automatically generates an init and string method for us
# can still customize the string method with __str if you want
@dataclass()
class Student:

    name: str
    school_id: str
    gpa: float
# def __init__(self, name, school_id, gpa):
# don't need init method with dataclass
# also don't need to use self with dataclass
# init is initialize
# any other variables you want to attribute to the class,
# you put in the parentheses with self
# self.name sets the student name variable to be associated with Student

    # def __str__(self):
    #     return f'Student: {self.name}, ID: {self.school_id}, GPA: {self.gpa}'
#     special method __str__ used to return a string representation of an object
# don't need this method since we are using dataclass


def main():
    alex = Student('Alex', '123456', '4.0')
    print(alex.name)
    print(alex.school_id)
    print(alex.gpa)
    # can identify which value in the class you want to print
    print(alex)
    # since __str was used, this will print a string now
    # changed that to dataclass, so there is no more __str
    sam = Student('Sam', '654321', '3.4')
    print(sam.name)
    print(sam.school_id)
    print(sam.gpa)
    print(sam)


if __name__ == '__main__':
    # this is for if you have multiple files running at the same time,
    # and you want to run a specific one from the cmd prompt
    # this doesn't make sense rn because we haven't learned it yet
    main()
# make sure to call your methods AFTER they are defined. otherwise nothing happens
