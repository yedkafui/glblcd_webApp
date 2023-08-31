# def Print_name():
#     return 'ug'

def edited(func):
    def wrap():
        cap_name = func()
        return cap_name.upper()
        
    return wrap


@edited
def Print_name():
    return 'josh'
   
upper = Print_name()
print(upper)   
        
