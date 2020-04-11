import abc

class SetGet:
    @abc.abstractmethod
    def se1t(self,val):
        self.val=val
        return
    
    @abc.abstractmethod
    def get():
        pass

class MyClass(SetGet):

    def get(self):
        print("Hello")

    def set1(self,val):
        self.val=val
        return val

c=MyClass()

c.get()
print(c.set1(32))