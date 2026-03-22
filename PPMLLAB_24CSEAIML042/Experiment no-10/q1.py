#WAP to demonstrate single inheritance where a child class inherits a method from a parent class.
class parent:
    def parent_method(self):
        print("Properties of parent")
class child(parent):
    def child_method(self):
        print("Properties of child")
ch=child()
ch.parent_method()
ch.child_method()