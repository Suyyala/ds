# learning class in python

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_grade(self):
        return self.grade
    
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
    
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        
        return value / len(self.students)
    

s1 = Student('Tim', 19, 95)
s2 = Student('Bill', 19, 75)
s3 = Student('Jill', 19, 65)

course = Course('Science', 2)
course.add_student(s1)
course.add_student(s2)
print(course.students[0].name)
print(course.get_average_grade())

# learning inheritance in python
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f'I am {self.name} and I am {self.age} years old')
    
    def speak(self):
        print('I dont know what I say')

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    
    def speak(self):
        print('Meow')
    
    def show(self):
        print(f'I am {self.name} and I am {self.age} years old and I am {self.color}')


class Dog(Pet):
    def speak(self):
        print('Bark')

class Fish(Pet):
    pass

p = Pet('Tim', 19)
p.show()
p.speak()

c = Cat('Bill', 34, 'Brown')
c.show()
c.speak()

d = Dog('Jill', 25)
d.show()
d.speak()

f = Fish('Bubbles', 10)
f.speak()


# learning multiple inheritance in python
class A:
    def __init__(self):
        super().__init__()
        print('Init A')
    
    def show(self):
        print('Show A')

class B:
    def __init__(self):
        super().__init__()
        print('Init B')
    
    def show(self):
        print('Show B')

class C(A, B):
    def __init__(self):
        super().__init__()
        print('Init C')
    
    def show(self):
        print('Show C')

c = C()
c.show()
print(C.mro())

