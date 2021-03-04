# A program of a simple calculator
#defining a function that adds two numbers
def add(x,y):
    return x+y

# a function that subtracts two numbers
def subtract(x,y):
    return x-y

# a function that multiplies two numbers
def multiply(x,y):
    return x*y

#a function that divides to numbers
def divide(x,y):
    return x/y
w = 'add'
x = 'subtract'
y = 'multiply'
z = 'divide'
print('w ={}'.format(w))
print('x ={}'.format(x))
print('y ={}'.format(y))
print('z ={}'.format(z))

while True:
    oper = input('Enter operation,w/x/y/z : ')
    if oper in ('w','x','y','z'):
        f_num = float(input('Enter first number : '))
        s_num = float(input('Enter second number : '))

        if oper=='w':
            print(f_num,'+', s_num, '=', add(f_num,s_num))
        elif oper=='x':
            print(f_num, '-', s_num, '=', subtract(f_num,s_num))
        elif oper=='y':
            print(f_num, '*', s_num, '=', multiply(f_num,s_num))
        elif oper=='z':
            print(f_num, '/', s_num, '=', divide(f_num,s_num))
        else:
            print('ENTER CORRECT OPERATION')
