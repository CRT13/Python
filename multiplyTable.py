"""
Simple Multiplication Table
"""
############################## Function Description ############################
def multiplyTable():
    #User-I/P Display
    print('==========================================')
    print('=========== Multiplication Table =========')
    print('==========================================')
    num = int(input("Please Enter Value of 'n': "))
    for i in range(1,11):
       print(num,'x',i,'=',num*i)
          
################################## Main Program ##################################
try:
    check = True
    while check:
        multiplyTable()
        check = int(input('Another Number?(1/0)'))
except:
    print('Error! Try Again')
##################################################################################


