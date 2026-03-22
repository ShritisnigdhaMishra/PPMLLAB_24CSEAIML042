#WAP using **kwargs
def employee(**details):
    for k,v in details.items():
        print(k,":",v)
employee(name="Shriti", id=101, dept="IT")