#class
#collection of attributes and methods
#object, class instance
 
class car:

    # constructor method

    def __init__(self,color,model,year) :
        self.color= color
        self.model= model
        self.year = year



#         # instantiate
# car1= car("Beige", "Dalmer", "1995")     
# print(car1.color) 

# car2=car("navy_blue", "ford_mustang","2005")

# print(car2.model)
    def describe(self):
        print(f"This is a {self.color},{self.year},{self.model}") 
        
car1= car("beige","Dlamer",1995)

car1.describe()

