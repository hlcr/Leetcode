class Singleton(object):
    _instance = 0
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

class MyClass(Singleton):
    a = 1
    def __init__(self):
        self.b = 0

if __name__ == '__main__':

    a = MyClass()
    b = MyClass()
    print(a == b)
