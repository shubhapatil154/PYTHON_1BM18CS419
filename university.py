class Student_info:
    def __init__(self):
        self.s_id = None
        self.s_age = None
        self.s_marks = None

    def setter(self):
         self.s_id = input('ENTER THE STUDENT ID: ')
         self.s_age = int(input('ENTER STUDENT AGE: '))
         self.s_marks =int(input('ENTER STUDENT MARKS: '))

    def validate_marks(self):
        if( self.s_marks>0 and  self.s_marks<100):
            return True
        else:
            return False

    def validate_age(self):
        if(self.s_age>20):
            return True
        else:
            return False

    def check_qualification(self):
        if(self.validate_marks()==True and self.validate_age()==True):
            if(self.s_marks>65):
               return True
            else:
               print('STUDENT MARKS IS NOT VALID FOR ADMISSION ')
               return False
        else:
            print('STUDENT IS NOT VALID FOR ADMISSION ')
            return False


    def getter(self):
        if(self.check_qualification() == True):
               print(f'THE STUDENT WITH ID {self.s_id} IS QUALIFIED FOR THE UNIVERSITY ADMISSION')
        else:
               print(f'THE STUDENT WITH ID {self.s_id} CANNOT BE QUALIFIED FOR THE UNIVERSITY ADMISSION')
               
               


S = Student_info()
S.setter()
S.getter()
                        
