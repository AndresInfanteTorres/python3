class vector:
    #the contructor of python is initialized everytime a "vector" object is created
    def __init__(self,px,py,pz):
        #the name of the variables "self.x,self.y,self.z" could be any name the importan is to equal them to the parameters that you are reciving (px,py,pz)
        self.x=px
        self.y=py
        self.z=pz
    #the pourpose of this function is to retunr a string of the values, if you do not use this function you get a "<__main__.vector object at 0x03075F70>"
    def __str__(self):
        return "(%f,%f,%f)"%(self.x,self.y,self.z)
    #here us the interesting part of operator overload, the firs parameter of the function is self and correspont to the vector "a" and the second parameter "parametro" correspond to the vector
    #b, and even if the second parameter name is "parametro", it also calls the method __init__ thats why you have to use the ".x,.y and .z at the end of parametro". So here is where the addition
    # occurs self.x+parametro.x and the saddition is store in the temporal variable tx.
    # So at the end of this operator overload you have to return an object with the results thats why we use "vector(tx,ty,tz)". 
    def __add__(self,parametro):
        tx=self.x+parametro.x
        ty=self.y+parametro.y
        tz=self.z+parametro.z
        return vector(tx,ty,tz)

a=vector(5,4,6)
b=vector(2,5,56)

print (a+b)

