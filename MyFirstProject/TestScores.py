from FractionTest import Fraction
from FractionTest import Percentage


def main():
    """Grades must be put in as fractions"""
    test1grade=Fraction(89,100)
    test2grade=Fraction(93,100)
    test3grade=Fraction(85,100)
    test4grade=Fraction(25,100)
    test5grade=Fraction(100,100)
    test1weight=Percentage(2,10)
    test2weight=Percentage(3,10)
    test3weight=Percentage(3,10)
    test4weight=Percentage(1,10)
    test5weight=Percentage(1,10)
    total=(test1grade*test1weight+test2grade*test2weight+test3grade*test3weight+test4grade*test4weight
           +test5grade*test5weight)
    pertotal=Percentage(total.num,total.den)

    print('You received a', pertotal,'on your tests.')

main()