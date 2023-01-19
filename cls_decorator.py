# clsDecorator.py

from datetime import datetime

class DateDecorator(object):
    # instance method decorator
    def instantMethodDecorator(self, func):
        def printDate(*args, **kwargs):
            print("Instance method decorator at time : \n", datetime.today())
            return func(*args, **kwargs)
        return printDate

    # class method decorator
    @classmethod
    def classMethodDecorator(self, func):
        def printDate(*args, **kwargs):
            print("Class method decorator at time : \n", datetime.today())
            return func(*args, **kwargs)
        return printDate


# decorator: instance method
a = DateDecorator()
@a.instantMethodDecorator
def add(a, b):
    return a+b

# decorator: class method
@DateDecorator.classMethodDecorator
def sub(a, b):
    return a-b

sum = add(2, 3)
# Instance method decorator at time :
#  2017-02-04 13:31:27.742283

diff = sub(2, 3)
# Class method decorator at time :
#  2017-02-04 13:31:27.742435
