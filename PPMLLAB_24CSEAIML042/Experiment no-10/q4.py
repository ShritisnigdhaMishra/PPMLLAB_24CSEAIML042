#WAP to demonstrate method overriding. Create a parent class and child class. Parent class has show method where the child class overrides the show method.
class parent:
    def show(self):
        print("Inside show method")
class child(parent):
    def show(self):
        print("Inside child show method")
ch=child()
ch.show()