class CSVFile:
    def __init__(self,name):
        self.name=name
        
        try:
            isinstance(self.name,str)==True
        except Exception as e:
            raise("Il nome del file non è una stringa, ma è "+e)
            
        self.can_read=True

        try:
            my_file=open(self.name,"r")
            my_file.readline()
        except Exception as e:
            self.can_read=False
            print("Errore in apertura del file: "+e)

    def get_data(self,start,end):

        if isinstance(start,float):
            start=int(start)
        else:
            try:
                isinstance(start,int)
            except Exception as e:
                print("Il carattere inserito per start è di tipo: "+e)
                return None
        
        if isinstance(end,float):
            end=int(end)
        else:
            try:
                isinstance(end,int)
            except Exception as e:
                print("Il carattere inserito per end è di tipo: "+e)
                return None

        start_pulito=start #.strip()
        end_pulito=end #.strip()

        if start_pulito>end_pulito:
            print("Errore lo start è maggiore dell'end")
            return None

        my_file=open(self.name,"r")
        lungezza=len(my_file.readlines())
        print (lungezza)
        if start_pulito not in range(0,lungezza) or end_pulito not in range(start,lungezza):
            print("Lo start o l'end non fanno parte della lungezza del file complessivo")
            return None
        
        if not self.can_read:
            print("Errore,file non aperto o illeggibile")
            
            return None

        else:
            data=[]

            my_file=open(self.name,"r")

            for i,line in enumerate(my_file):

                if i in range(start-1,end):
                
                    elements=line.split(",")

                    elements[-1]=elements[-1].strip()

                    if elements[0] !="Date":
                        data.append(elements)

            return data

lol=CSVFile("shampoo_sales.csv")
print(lol.get_data(20,30))



class NumericalCSVFile(CSVFile):
    
    def get_data(self):
        
        string_data=super().get_data()

        numerical_data=[]

        for string_row in string_data:

            numerical_row=[]

            for i,element in enumerate(string_row):

                if i==0:
                    
                    numerical_row.append(element)
                    
                else:
                    
                    try:
                        
                        numerical_row.append(float(element))
                        
                    except Exception as e:
                        print("Errore in conversione del valore " + element +" a numerico: "+e)
                        break

            if len(numerical_row)==len(string_row):
                numerical_data.append(numerical_row)

        return numerical_data
                    

        
                
            