def first():
    a="hello local"
    print(a)
first()


x="jobayer global"
def second():
    global x
    x="hello"
second()
print(x)

x="jobayer global"
def second():
    print(x)
second()


def test():
    y = 50

test()
print(y)   # ❌ ERROR: y is not defined


