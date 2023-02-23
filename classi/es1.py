
class CSVFile():
    def __init__(self,name):
        self.name=name
        
    def get_data(self):
        my_file=open(format(self.name), "r")
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
        
#my_file=open("shampoo_sales.csv", "r")
#lol=CSVFile(my_file)
#print(lol.get_data())