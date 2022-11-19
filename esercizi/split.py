

def sum_csv(file_name):
    
    my_file=open(file_name, "r")
    
    value=[]
    
    for line in my_file:

        element=line.split(",")

        if element[0] == "Date":
            continue

        value.append(float(element[1]))

    return sum(value)  
            
