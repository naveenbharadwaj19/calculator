# from kivy.app import App
# from kivy.uix.label import Label
# from kivy.uix.button import Button

class Calculator():
    def __init__(self):
        self.x = int(input("Enter a number:\n"))
        self.y = int(input("Enter a number:\n"))
    def add(self):
         return self.x + self.y
    
    def subtraction(self):
        return self.x - self.y
    
    def multiplication(self):
        return self.x * self.y

    def divide(self):
        try:
            return self.x /self.y
        except ZeroDivisionError:
            return "Math Error"

flag = True
while flag:
    choice = int(input("Press 1 -- add , 2 -- sub 3 -- multiply 4 -- divide , --- any other number to exit:\n"))
    if choice == 1:
        calculator = Calculator()
        print("Answer: " + str(calculator.add()))
    elif choice == 2:
        calculator = Calculator()
        print("Answer: " + str(calculator.subtraction()))
    elif choice == 3:
        calculator = Calculator()
        print("Answer: " + str(calculator.multiplication()))
    elif choice == 4:
        calculator = Calculator()
        print("Answer: " + str(calculator.divide()))
    else:
        print("Exiting!")
        flag = False
