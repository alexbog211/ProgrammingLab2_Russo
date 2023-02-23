class MovingAverage():
    def __init__(self,window):
        self.window=window
        
        if not type(self.window) is int:
            raise ExamException("La lunghezza inserita della lista non è un numero intero")

        if self.window <= 0:
            raise ExamException("La lunghezza della lista è 0 o negativa")
            
    def compute(self, list):
            
        medie_mobili=[]
        
        if list==None:
            raise ExamException("La lista ha il valore None")

        if type(list) != type(medie_mobili):
            raise ExamException("La lista inserita non è una lista")
            
        lung=len(list)

        if lung < self.window:
            raise ExamException("La lunghezza della finestra è maggiore della lista")

        for x in list:
            if type(x) != int  and type(x) != float:
                raise ExamException("La lista contiene almeno un elemento che non è numerico")
                
        for i,x in enumerate(list):
            valori=[]
            media=[]
            for y in range(self.window):
                valori.append(list[i+y])

            media=sum(valori)/self.window
            medie_mobili.append(media)

            if i==lung-self.window:
                break
        return medie_mobili
            
class ExamException(Exception):
    pass

#moving_average=MovingAverage(2)
#result=moving_average.compute([2,4,8,16,18,20])
#print(result)