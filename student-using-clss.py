class stud:
    def __init__(self,a,b,c):
        self.sno=a
        self.sname=b
        self.sdept=c
    def disp(self):
        print("student rollno:",self.sno)
        print("student nmae:",self.sname)
        print("student dept:",self.sdept)

s=int(input("enter the the roll no:"))
d=input("enter the student name:")
f=input("enter the deparetment:")
ob=stud(s,d,f)
ob.disp()
