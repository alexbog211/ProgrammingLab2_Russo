class CSVFile():
    def __init__(self,name):
        self.name=name
        
    def get_data(self):
        my_file=0
        try:
            my_file=open(format(self.name), "r")
        except:
            print("Errore, il file non esiste")
            return "mona"
        value=[]

        for line in my_file:
            element=line.strip()
            lungezza=len(element)
            #line_vuoto=os.path.getsize(line)
            if(lungezza !=0):
                element=element.split(",")
                if element[0] == "Date":
                    continue
                value.append(element)
        return value

class NumericalCSVFile(CSVFile):
    def __init__(self,name):
        super().__init__(name)
        
    def flo(self):
        my_value=super().get_data()
        my_flat=[]
        for item in my_value:
            try:
                item[1]=float(item[1])
            except:
                print("L'elemento non può essere convertito a float")
                continue
            
            
                
            
    
lol=NumericalCSVFile("shampoo_sales.csv")
print(lol.flo())