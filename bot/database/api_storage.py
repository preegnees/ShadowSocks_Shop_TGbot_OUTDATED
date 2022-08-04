from loguru import logger

class IStorage:
    def func1(self):
        pass
 
    def func2(self):
        pass
 
 
class Test(IStorage):
    def func1(self):
                 print ('Переписать функцию1')
 
    def func2(self):
                 print ('Переписать функцию2')
 
    def func3(self):
                 print ('Недавно добавленная функция3')