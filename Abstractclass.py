from abc import ABC,abstractmethod

class parent(ABC):
    def property(self):
        pass



class child(parent):
    def property(self):
        print('hello')


a=child()
a.property()
 
