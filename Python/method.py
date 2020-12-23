
class Student:
    school = ' Roosevelt'

    def __init__(self, m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def average (self):
        return (self.m1 + self.m2 + self.m3) / 3

    @classmethod
    def getSchool (cls):
	    return cls.school
    @staticmethod
    def info():
	    print( 'This is nw schedule ')


    #@classmethod          # @ this is the decorator if using the class method variable
    #def info (cls):       # Working with a class variable need to use the cls it is a key word
	 #   return cls.school



s1 = Student (34,37,32)

s2= Student (89,32,12)

print (s1.average())

print (s2.average())
print(Student.getSchool())

Student.info()
##########################################################


''' *Instance method *Class method and *static variables. IF you pass the self it is the instance method it belongs
 to an objectso the average in the above is the instance method Instance has two types Accessor
  just fetch the values or  getter and the setterget set  getter or get the value or getter fetch the value
&  Mutators Modifiers Methods Modifies. so they are setter change the value and so called muttator
Static method are used when not working with instance or class variable then use the class variable'''

