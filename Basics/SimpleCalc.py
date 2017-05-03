""" SimpleCalc: Four-Function Calculator """
#################### FUNCTION INITIALIZATIONS ###################
def Add(x,y):
    print('Sum = ',x+y)
def Sub(x,y):
    print('Difference = ',x-y)
def Mul(x,y):
    print('Product ',x*y)
def Div(x,y):
    print('Quotient = ',x/y)
#################################################################
########################## MAIN PROGRAM #########################
legalTup = (1,2,3,4)
flag = 0
restart = 1
print('This Is A Simple Calculator')
while restart:
    print('==== Choose Functionality ====')
    print('Add (1)\nSubstract (2)\nMultiply (3)\nDivide (4)')
    usrInput = int(input('Choose Option (1-4): '))
    print('==============================')
    for i in range(0,4):
        if (usrInput == legalTup[i]):
            flag = 1
            break
    if flag == 0:
        print('Incorrect Response, Try Again!')
    else:
        print('Enter Values of (x,y): ')
        x = float(input())
        y = float(input())
        if usrInput == 1:
            Add(x,y)
        elif usrInput == 2:
            Sub(x,y)
        elif usrInput == 3:
            Mul(x,y)
        else:
            Div(x,y)
    rst = input('Restart? (y|n)')
    if (rst == 'y' or rst == 'Y'):
        restart = 1
    elif (rst == 'n' or rst == 'N'):
        restart = 0
    else:
        print('Invalid Choice!')
        break
#################################################################
