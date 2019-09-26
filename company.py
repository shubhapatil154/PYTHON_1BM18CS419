class Call_Detail:
    def __init__(self):
        self.dailer = None
        self.receiver = None
        self.call_duration = None
        self.call_type = None

    def set_details(self,y):
        self.dailer = y[0]
        self.receiver = y[1]
        self.call_duration = y[2]
        self.call_type = y[3]
        self.get_details()
    def get_details(self):
        print(self.dailer.ljust(20),end=" ")
        print(self.receiver.ljust(20),end=" ")
        print(self.call_duration.ljust(20),end=" ")
        print(self.call_type.ljust(20))
        
class Util:
    def __init__(self):
        self.list_of_call_Objects= []

    def Parse_Customer(self,list_of_call_string):
        for x in range(len(list_of_call_string)):
            y=list_of_call_string[x].split(",")
            self.list_of_call_Objects.append(CallDetail())
            self.list_of_call_Objects[x].set_details(y)
            


call1='9999012375,93330000104,23,STD'
call2='7418596301,7531234589,54,Local'
call3= '9991110001,7531478965,6,ISD'
list_of_call_string=[call1,call2,call3]

print("DIALER".ljust(20),end=" ")
print("RECIEVER".ljust(20),end=" ")
print("CALL_DURATION".ljust(20),end=" ")
print("CALL_TYPE".ljust(20))
Util().parse_customer(list_of_call_string)
