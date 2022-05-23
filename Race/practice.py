class Robot:
    def __init__(self,name,color,weight):#constructor
        self.name=name
        self.weight=weight
        self.color=color
    def introduce_self(self): #method (with argument)
        print(' my name is ' + self.name)
        print('im ' + self.color +' in colour')
        print('my weight is '+ str (self.weight))



r1=Robot("varun", 'brown' , 110)#creating object
r1.introduce_self()# calling method in class
