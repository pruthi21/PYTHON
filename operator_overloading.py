'''If any operator performs additional action or behavior other than what is meant for then it is called operator overloading.
'''
class Point1:
    def __init__(self, x):
        self.x = x
        
    def __add__(self, other):      
        return self.x + other.x
        

class Point2:
    def __init__(self, x):
        self.x = x

p1 = Point1(10)
p2 = Point2(20)


print(p1+p2)     #Point1.__add__(self, other)