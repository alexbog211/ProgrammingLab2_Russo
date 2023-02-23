class CSVFile():
    def __init__(self,name):
        self.name=name
        
    def get_data(self):
        my_file=0
        try:
            my_file=open(format(self.name), "r")
        except:
            print("Errore, il file non esiste")
            return 1
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
             
     

lol=CSVFile("shampoo_sales.csv")
print(lol.get_data())