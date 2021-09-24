import math
import matplotlib as plt
class Operator:
    def __init__(self):
        self.index2operator = {
        '1':self.add,
        '2':self.subtract,
        '3':self.multiply,
        '4':self.divide,
        '5':self.sin,
        '6':self.log,
        }
    
    def add(self, *args):
        return sum(args)
    
    def subtract(self, *args):
        x, y = args[0], sum(args[1:])
        return x - y

    def multiply(self, *args):
        m=1.0
        for n in args:
            m=n*m
        return m
    
    def divide(self, *args):
        return args[0] / args[1]
    
    def sin(self, *args):
        return math.sin(args[0])
    def log(self,*args):
        return math.log(args[0],args[1])
    
    
    def _func(self, operIdx, *args):
        operator = self.index2operator[operIdx]
        return operator(*args)
    def _plot(self,operIdx,*ran):
        xp = [*range(ran[0], ran[1], 0.1)]
        yp = oper._func(choice,*xp)
        plt.plot(xp,yp)

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.sin")
print("6.log")

while True:
    # take input from the user
    oper = Operator()
    choice = input("Enter choice(1/2/3/4/5/6): ")
    
    try:
        assert choice in oper.index2operator
    except:
        print('This operator is not available.')
        raise ValueError
    
    if choice != '5':
        nums = input(f'Enter two numbers to {oper.index2operator[choice].__name__}(seperated by comma. [E.g: 1,2] ):').split(',')
        nums = [float(n) for n in nums if n != '']
    elif choice == '6':        
        nums = input(f'Enter two numbers to {oper.index2operator[choice].__name__}(seperated by comma. [E.g: ln2 == 2,10]):').split(',')     
        ran = input(f'Enter two numbers to for the range of {oper.index2operator[choice].__name__} graph(seperated by comma. [E.g: 1,2] ):').split(',')
        nums = [float(n) for n in nums if n != '']
        ran = [float(n) for n in ran if n != '']
        xp = [*range(ran[0], ran[1], 0.1)]
        yp = oper._func(choice,*xp)
        globals(xp)

    else:
        print(f'Enter one number to {oper.index2operator[choice].__name__}:')
        num1 = float(input())
        num2 = None

    oper._plot(choice,*ran)
    res = oper._func(choice, *nums)
    print(f'Result: {res}')
    another=input('wanna do another calculation? (y/n)')
    if another=='n':
        break
    else:
        pass