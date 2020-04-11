class ClassA:
    _param1=200
    def __init__(self):
        self._param1=100
    def method1(self):
        ClassA._param1=(ClassA._param1+1)+(self._param1+1)

    @staticmethod
    def method2():
        print(ClassA._param1)

obj1=ClassA()

print(type(obj1.method1()))