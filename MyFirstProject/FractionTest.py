class Fraction:

    def __init__(self,num,den):
        self.num=num
        self.den=den
        common=gcd(num,den)
        self.num=num//common
        self.den=den//common

    def __str__(self):
        #puts numbers into a readible "a/b" format
        return(str(self.num)+"/"+str(self.den))

    def __add__(self, other):
        #adds two fractions together
        num2=self.num*other.den + self.den*other.num
        den2=self.den*other.den
        return Fraction(num2,den2)

    def __sub__(self, other):
        #subtracts two fractions together
        num2=self.num*other.den - self.den*other.num
        den2=self.den*other.den
        return Fraction(num2,den2)

    def __mul__(self, other):
        #multiply two fractions together
        num2=self.num*other.num
        den2=self.den*other.den
        return Fraction(num2,den2)

    def __truediv__(self, other):
        #divide two fractions together
        num2=self.num*other.den
        den2=self.den*other.num
        return Fraction(num2,den2)

    def __cmp__(self,other):
        #compare two fractions together, returns neg if self<other, pos if self>other, zero if ==
        num1=self.num*other.den
        num2=self.den*other.num
        return(num1-num2)

    def __eq__(self,other):
        return self.__cmp__(other) == 0

    def __ne__(self,other):
        return not self == other

    def __lt__(self,other):
        return(self.__cmp__(other))<0

    def __le__(self, other):
        return(self.__cmp__(other))<=0

    def __gt__(self, other):
        return(self.__cmp__(other))>0

    def __ge__(self, other):
        return(self.__cmp__(other))>=0

class Percentage(Fraction):
        def __str__(self):
            return (str(self.num / self.den * 100) + "%")





def gcd(a,b):
    #determines GCD of the fraction for reduction
    while a%b != 0:
        olda = a
        oldb = b

        a = oldb
        b = olda%oldb
    return b




def main():
    #inputs two fractions and finds various functions
    global w
    global x
    global y
    global z
    f1=Fraction(w,x)
    f2=Fraction(y,z)
    print('f1=',f1)
    print('f2=',f2)
    print('f1+f2=',f1+f2)
    print('f1-f2=',f1-f2)
    print('f1*f2=',f1*f2)
    print('f1/f2=',f1/f2)
    print('Is f1<f2?',f1<f2)
    print('Is f1<=f2?',f1<=f2)
    print('Is f1>f2?',f1>f2)
    print('Is f1>=f2?',f1>=f2)
    print('Is f1==f2?',f1==f2)
    print('Is f1!=f2?',f1!=f2)
    x1=Percentage(w,x)
    x2=Percentage(y,z)
    print('Your first fraction\'s percent is',x1)
    print('Your second fraction\'s percent is',x2)

w=input("What is the numerator of the first fraction?")
x=input("What is the denomenator of the first fraction?")
y=input("What is the numerator of the second fraction?")
z=input("What is the denominator of the second fraction?")
w=int(w)
x=int(x)
y=int(y)
z=int(z)

main()

