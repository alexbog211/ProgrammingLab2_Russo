class Model:
    def __init__(self,data=""):
        self.data=data
        self.can_read=True
        
       try:
           isinstance(self.data,str)
       except BaseException as e:
            raise('Il nome del file non è una stringa, ma è: "{}"'.format(e))
            
        try:
            my_file=self.data
            my_file.readline()
        except BaseException as e:
            self.can_read=False
            raise('Errore in apertura del file: "{}"'.format(e))

        for line in my_file:
            try:
                int(line)
            except: 
                raise("Il file contiene a riga "+line+" un carattere non float" )


        
        
            
    def fit(self,data):
        raise NotImplementedError("Metodo non implementato")
    def predict(self,data):
        raise NotImplementedError("Metodo non implementato")

#lol=Model("prova.txt")

class IncrementModel(Model):
    
    def predict(self,data):
        
        my_file=self.data
        new_file=self.data
        prev_value=0
        first_value=0
        last_value=0
        lung=len(new_file.readlines())
        
        for i,item in enumerate(my_file):
            
            if i==0:
                first_value=item
                
            elif i < lung:
                prev_value=prev_value+item-first_value
                first_value=item
                
            if i==lung-1:
                last_value=item
                
        prev_value=prev_value/(lung-1)
        return prev_value+last_value


#print(lol.predict())