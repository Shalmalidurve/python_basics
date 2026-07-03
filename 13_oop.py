class Student():
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
    def display(self):
        print(self.name,":",self.marks)

    def grade(self):
        if self.marks>=90:
            print("Grade is A+\n")
        elif self.marks>=75 and self.marks<90:
            print("Grade is B\n")
        elif self.marks>=60 and self.marks<75:
            print("Grade is C\n")
        else:
            print("fail\n")

        return()
    

s=Student("Anaya",85)
s1=Student("Rahul",95)
s2=Student("Mira",35)
s1.display()
s1.grade()
s.display()
s1.grade()
s2.display()
s2.grade()
