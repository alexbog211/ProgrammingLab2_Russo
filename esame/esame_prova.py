class ExamException(Exception):
    pass

class CSVTimeSeriesFile:
    def __init__(self,name):
        self.name=name
            
    def get_data(self):

        try:
            my_file=open(self.name,"r")
            my_file.readline()
        except:
            raise Exception("Errore di apertura del file")
            
        my_file=open(self.name, "r")
        new_file=[]
        
        for line in my_file:
            elements=line.split(",",1)
            elements[-1]=elements[-1].strip()
            date=elements[0].split("-",1)
            if elements[0] != "date" and len(elements)==2 and len(date)==2:
                if elements[-1].isnumeric() and date[0].isnumeric() and date[1].isnumeric():
                    elements[-1]=int(elements[-1])
                    new_file.append(elements)
                else: 
                    pass
        print(*new_file, sep="\n")
                    
        # inizio controllo ordinamento
        list_length=len(new_file)
        for x in range(list_length):
            element_zero=new_file[x]
            element_zero=element_zero[0].split("-")
            year_zero=int(element_zero[0])
            month_zero=int(element_zero[1])
            for i in range(x+1,list_length):
                control_element=new_file[i]
                control_element=control_element[0].split("-")
                control_year=int(control_element[0])
                control_month=int(control_element[1])

                if control_year<year_zero:
                    raise Exception("Gli elementi non sono ordinati per anno")
                if control_year<=year_zero and control_month<month_zero:
                    raise Exception("Gli elementi: "+str(year_zero)+"-"+str(month_zero)+" e "+str(control_year)+"-"+str(control_month)+" non sono ordinati per mese")
                if control_year==year_zero and control_month==month_zero:
                    raise Exception("Esiste un doppione")  
        #fine controllo ordinamento            
        return new_file
            
time_series_file=CSVTimeSeriesFile("data.csv")
time_series=time_series_file.get_data()


years=["1949","1950"]

def detect_similar_monthly_variations(time_series, years):

    if len(years)!=2:
        raise Exception("La lista di anni non contiene due elementi")
        
    for idx,year in enumerate(years):
        
        if isinstance(year,int)==False:
            try:
                years[idx]=int(years[idx])
            except:
                raise Exception("L'anno inserito non è un numero intero")
    for idx,year in enumerate(years):        
        if year<0:
            raise Exception("L'anno inserito è un numero negativo")
        if idx==0 and years[idx+1]!=years[idx]+1:
            raise Exception("I due anni non sono consecutivi")
    errore=2
    year_one=[]
    year_two=[]
    for x in range(2):
        for i in range(12):
            if x==0:
                year_one.append(None)
            else:
                year_two.append(None)

    flag1=None
    flag2=None
    for idx,year in enumerate(years):
        for element in time_series:
            value=element[1]
            data=element[0]
            data=data.split("-")
            data[0]=int(data[0])
            data[1]=int(data[1])
            if data[0]==year and idx==0:
                flag1=0
                year_one[data[1]-1]=value
            if data[0]==year and idx==1:
                flag2=0
                year_two[data[1]-1]=value
                
    if flag1!=0 or flag2!=0:
        raise Exception("Gli anni inseriti non fanno parte della lista")
        
    double_year=[year_one,year_two]
    #print(*year_one,sep="\n")
    #print(*year_two,sep="\n")
    var1=[]
    var2=[]
    for idx,year in enumerate(double_year):
        for pas in range(0,11):
            if year[pas]!=None and year[pas+1]!=None:
                diff=year[pas+1]-year[pas]
                if idx==0:
                    var1.append(diff)
                else:
                    var2.append(diff)
            else:
                if idx==0:
                    var1.append(None)
                else:
                    var2.append(None)
 
                
    print(var1)
    print(var2)
    similar=[]
    for x in range(0,11):
        if var1[x]==None or var2[x]==None:
            similar.append(False)
        else:
            if var1[x]==var2[x]:
                similar.append(True)
            elif abs(var1[x]-var2[x])<=errore:
                similar.append(True)
            else:
                similar.append(False)
    return similar

print(detect_similar_monthly_variations(time_series,years))
