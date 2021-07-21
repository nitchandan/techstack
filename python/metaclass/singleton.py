class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        print(cls)
        print(cls._instances)
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Foo(metaclass=Singleton):
    pass

class Zoo(metaclass=Singleton):
    pass

class NonFoo():
    pass


if __name__ == '__main__':
    print(Foo() == Foo())
    print(Zoo())
    print(NonFoo() == NonFoo())