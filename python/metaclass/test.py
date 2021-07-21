class Foo:
    pass

if __name__ == '__main__':
    obj = Foo()
    print("class  of object  Foo using type:",type(obj))
    print("class of object using __class__",obj.__class__)
    print(type(obj) == obj.__class__)