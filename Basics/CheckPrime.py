""" CheckPrime: Prime Number Checker """
#################### FUNCTION INITIALIZATIONS ###################
def checkPrime():
    #User-I/P Display
    print('==========================================')
    print('=========== Prime Number Checker =========')
    print('==========================================')
    num = int(input("Please Enter Value of 'n': "))
    if num > 1:
      for i in range(2,num):
         if (num % i) == 0:
              print(num,'is composite!')
              print(i,'x',num//i,'=',num)
              break
      else:
          print(num,'is prime!')
    else:
      print(num,'is not a prime number!')
#################################################################
########################## MAIN PROGRAM #########################
try:
    check = True
    while check:
        checkPrime()
        check = int(input('Another Number?(1/0)'))
except:
    print('Error! Try Again')
#################################################################

