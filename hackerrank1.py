class Complex(object):
    def __init__(self, real, imaginary):
        self.real=real
        self.imaginary=imaginary

    def __add__(self, no:"Complex"):
        sum_imaginary = self.imaginary + no.imaginary
        sum_real = self.real + no.real
        sum=Complex(real=sum_real, imaginary=sum_imaginary)
        return sum
    
    def __sub__(self, no:"Complex"):
        sub_imaginary = self.imaginary - no.imaginary
        sub_real = self.real - no.real
        sub=Complex(real=sub_real, imaginary=sub_imaginary)
        return sub
    
    def __mul__(self, no:"Complex"):
        mul_real= (self.real*no.real)-(self.imaginary*no.imaginary)
        mul_imaginary=(self.real*no.imaginary)+(self.imaginary*no.real)
        mul=Complex(real=mul_real, imaginary=mul_imaginary)
        return mul
    
    def __truediv__(self, no:"Complex"):
        div_real= ((self.real*no.real)+(self.imaginary*no.imaginary))/((no.real**2)+(no.imaginary**2))
        div_imaginary=((self.imaginary*no.real)-(self.real*no.imaginary))/((no.real**2)+(no.imaginary**2))
        div=Complex(real=div_real, imaginary=div_imaginary)
        return div
    
    def mod(self):
        mod=((self.real**2)+(self.imaginary**2))**(1/2)
        return Complex(real=mod, imaginary=0)
    
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
    c = map(float, input("Enter number 1: ").split())
    d = map(float, input("enter number 2: ").split())

    x = Complex(*c)
    y = Complex(*d)

    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')  