class Diff():
    def __init__(self,ratio=1):
        self.ratio=ratio

        
        if type(self.ratio) != int and type(self.ratio) != float:
            raise ExamException("Il valore di ratio non è numerico")
        if self.ratio<=0:
            raise ExamException("Il valore ratio è minore o uguale a zero")
    def compute(self,list):
        new=[]
        if list==None:
            raise ExamException("La lista ha il valore None")

        if type(list) != type(new):
            raise ExamException("La lista inserita non è una lista")
        if len(list)<=1:
            raise ExamException("La lista è troppo corta")
        for x in list:
            if type(x) != int  and type(x) != float:
                raise ExamException("La lista contiene almeno un elemento che non è numerico")
                
        for i in range(len(list)-1):
            differenza=(list[i+1]-list[i])/self.ratio
            new.append(differenza)
        return new
class ExamException(Exception):
    pass