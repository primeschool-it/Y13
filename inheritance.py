## Inheritance
class Student():
    def __init__(self, student_name, student_age, student_dob):
        print("instanciating member....",student_name)
        self.name = student_name
        self.age = student_age
        self.dob =  student_dob
        self.session = '2020-2021'

    def get_subjects(self):
        print(" Hi %s, Your Subjects are below" % self.name)
        return 'Math, Science, English, History, Art'


class Y01(Student):
    pass

class Y02(Student):
    pass

class Y03(Student):

    pass
class Y04(Student):
    pass
class Y05(Student):
    pass

class Y13(Student):
    pass
    # def __init__(self, subject_list):
    #     self.subjects = subject_list
    def get_subjects(self):
        ## Do not call super if you want to replace the property
        ## Call super only if you want to modify result of super
        subject_list = super(Y13, self).get_subjects()
        subject_list = subject_list + ',Career Program'
        print (" Hi %s, Your Subjects are below" %self.name)
        return subject_list

# cao = Student('Cao', 17, '2003-03-26')
lisa = Y05('Lisa', 12, '2008-03-26')
cao = Y13('Cao', 17, '2003-03-26')
lisa_subjects = lisa.get_subjects()
print(lisa_subjects)
cao_subjects = cao.get_subjects()
print(cao_subjects)
print()