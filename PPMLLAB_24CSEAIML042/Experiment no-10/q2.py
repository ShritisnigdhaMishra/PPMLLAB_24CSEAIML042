#WAP to demonstrate multilevel inheritance classes grandparent with methods property, parent(business()), child(education()).
class grandparent:
    def gp_property(self):
        print("Inside grandparent method")
class parent(grandparent):
    def business(self):
        print("Inside parent business method")
class child(parent):
    def education(self):
        print("Inside child education method")
ch=child()
ch.gp_property()
ch.business()
ch.education()