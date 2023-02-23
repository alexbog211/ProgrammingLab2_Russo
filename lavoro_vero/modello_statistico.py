class Modello():
    def __init__(self,name):
        self.name=name

        try:
            my_file=open(self.name, "r")
        except:
            raise "Il programma non è riuscito a aprire il file"

    def fit():
        pass;

    def evaluate():
        pass

class Clean(Modello):
    def __init__(self,name):
        super.__init__(name)
        
    def clean(self):
        old_file=open(format(self.name),"r")
        new_file=[]
        len=0

        for line in old_file:
            len +=1
            elements=line.split(",")
            elements[-1]=elements[-1].strip()

            if elements[0] != "Date":
                new_file.append(elements[-1])
        self.name=new_file
        self.len=len

        print(self.name)
        print(self.len)

primo=Modello("shampoo_sales.csv")

class Fit(Clean):
    