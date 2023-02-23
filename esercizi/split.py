      
def sum_csv(file_name):
    
    # my_file=open(file_name, "r")

    value=[]
    
    for line in file_name:

        element=line.split(",")

        if element[0] == "Date":
            continue

        value.append(float(element[1]))

    return sum(value)  

my_file=open("shampoo_sales.csv", "r")
print(sum_csv(my_file))