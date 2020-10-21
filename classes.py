# 1.Classes
# 2. Objects or Instance or Class Members
# 3. Properties of Objects
# 4. Getting Values from Objects
# 5. Setting Values to Objects
# 6. Deleting an object

class Y11():
    ###Initialization of the class
    def __init__(self, student_name, student_age, student_dob):
        self.name = student_name
        self.age = student_age
        self.dob =  student_dob
        self.batch_start_date = '2020-08-01'


class Y12():
    ###Initialization of the class
    def __init__(self, student_name, student_dob):
        self.name = student_name
        self.dob =  student_dob
        self.batch_start_date = '2020-08-01'

## Instance of the class
a = Y11('A', 11, '2000-01-01')
b = Y11('B', 12, '2000-05-04')


e = Y12('E', '2000-01-01')
f = Y12('F',  '2000-05-04')


## Set Property of an object
a.address = 'Estoril'
## Get Property of an object
a.age

## deleting an object
del a
print()