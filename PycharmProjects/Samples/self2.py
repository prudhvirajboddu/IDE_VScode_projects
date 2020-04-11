class ClassA:
    _param1=200
    def __init__(self):
        self._param1=100

    @staticmethod
    def method():


obj1=ClassA()

print(ClassA._param1)

print(ClassA.method())