from Stack import myStack

def main():

    theStack = myStack()
    done = False
    
    print("This program will match parentheses, brackets, and braces.")
    print("The input can be anything.  All symbols in the input", end = " ")
    print("will be ignored except the parenthese, brackets, and braces.")

    print("\nEnter any expression that contains parentheses, brackets, ")
    inputString = input("and braces (empty string to quit): ")
    if (inputString == ""):
        done = True

    while (not done):

        for symbol in inputString:
            # push left-hand symbols on the stack
            if (symbol == '(' or symbol == '[' or symbol == '{'):
                theStack.push(symbol)

            # if we see a right-hand symbol, make sure the symbol
            # on the top of the stack matches. If the stack is
            # empty, then clearly they don't match

            elif(symbol == ')'):
                if (theStack.isEmpty()):
                    print ("Parentheses do not match.")
                    break

                matchingSymbol = theStack.pop()
                if (matchingSymbol != '('):
                    print ("Parentheses do not match.")
                    break

            elif(symbol == ']'):
                if (theStack.isEmpty()):
                    print ("Parentheses do not match.")
                    break

                matchingSymbol = theStack.pop()
                if (matchingSymbol != '['):
                    print ("Brackets do not match.")
                    break

            elif(symbol == '}'):
                if (theStack.isEmpty()):
                    print ("Parentheses do not match.")
                    break

                matchingSymbol = theStack.pop()
                if (matchingSymbol != '{'):
                    print ("Braces do not match.")
                    break

            # else ...  ignore all other symbols


	# Once we are done processing the input, the stack had better be
        # empty.  If not, then there was an open symbol without a closing one.

        if (not theStack.isEmpty()):
            print("symbol", theStack.peek(), "was not closed")

            # We need to empty the stack before processing the next input
            # or else we will misinterpret a non-empty stack as an error

            while (not theStack.isEmpty()):
                theStack.pop()
        else:
            print("Parenthese, brackets, and braces match.")

        print("\nEnter any expression that contains parentheses, brackets, ")
        inputString = input("and braces (empty string to quit): ")
        if (inputString == ""):
            done = True


main()


        
