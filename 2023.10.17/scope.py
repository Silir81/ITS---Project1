a = 1


# Uses global because there is no local 'a'
def f():
    print('Inside f() : ', a)


# Variable 'a' is redefined as a local
def g():
    a = 2
    print('Inside g() : ', a)


# Uses global keyword to modify global 'a'
def h():
    def g1():
        print()
        def g2():
            pass
    global a
    a = 3
    g1()
    print('Inside h() : ', a)


# Global scope
print('global : ', a)   #Printeaza variabila (globala) a
f()
print('global : ', a)
g()
print('global : ', a)
h()
print('global : ', a)
g2()