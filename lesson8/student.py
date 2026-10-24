class Student:
    def __init__(self,name,major,gender,math,physics,chem):
        self.name=name
        self.major=major
        self.gender=gender
        self.math=math
        self.physics=physics
        self.chem =chem

    def greet(self):
        print(f"students name is {self.name},he/she studies{self.major},and his/her gender is {self.gender}")

    def mesatarja(self):
        print(f"{self.name} avrage is {(self.math+self.physics+self.chem)/3}")

student1 = Student("enes","proggraming","m",7,8,9)
student2 = Student("elmaze","math","f",10,6,9)

student1.greet()
student2.greet()

student1.mesatarja()
student2.mesatarja()