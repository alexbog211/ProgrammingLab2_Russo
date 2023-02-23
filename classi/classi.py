class Person():

    def __init__(self,name,sexuality):
        self.name=name
        self.sexuality=sexuality

    def __str__(self):
        return (self.name +" is "+ self.sexuality)


person=Person("Liam", "gay")
print(person)
#print(person.name + person.sexuality)