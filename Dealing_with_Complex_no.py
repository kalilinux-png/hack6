import math
class Complex(object):
    def __init__(self, real, imaginary):
        self.real=real
        self.imaginary=imaginary
        
    def __add__(self, no):
        self.real=self.real+no.real
        self.imaginary= self.imaginary+no.imaginary
    def __sub__(self, no):
        self.real=self.real-no.real
        self.imaginary=self.imaginary-no.imaginary
        
    def __mul__(self, no):
        self.real=self.real*no.real-self.imaginary*no.imaginary
        self.imaginary=self.real*no.imaginary+self.imaginary*no.real
        

    def __truediv__(self, no):
        ac=self.real*no.real
        bd=self.imaginary*no.imaginary
        bc=self.imaginary*no.real
        print(type(self.real),type(no.imaginary))
        print(self.real,no.imaginary)
        ad=self.real*(no.imaginary*-1)
        square_c_d=2*no.imaginary+2*no.real
        self.real=ac+bc
        self.imaginary=bd+bc
        

    def mod(self):
        self.real=abs(self.real**2)
        self.imaginary=abs(self.imaginary**2)
        
        self.real=math.sqrt(self.real+self.imaginary)
        

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
