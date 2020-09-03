class Cont():
    def __init__(self, cont1=0):
        self.cont1 = cont1

    def add(self, num=0):
        num = int(input("How much to add? [0 if you don't want to add anything] "))
        self.cont1 += num

    def reduce(self, num2=0):
        num2 = int(input("How much to reduce? [0 if you don't want to reduce anything] "))
        self.cont1 -= num2
    
    def seeCont(self):
        print(f'Your counter is currently {self.cont1}! ')

cont = Cont()