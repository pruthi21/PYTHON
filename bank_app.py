from abc import ABC, abstractmethod

class intrestcal(ABC):
    @abstractmethod
    def cal_simple_intrest(self,rate,time, rule):
        pass
    @abstractmethod
    def total_amount(self, rule, intrest):
        pass

class simpleintrest(intrestcal):