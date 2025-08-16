#string is a sequence of characters 

name= "hello world"

#slicing and indexing
# print(name[-3:-2])
 
 #f string
name = "Dorice"
course = "python"

# for i in name :
    #  print(i)

txt = "the best things in life are free"

# print("free" in txt)

# print("things"not in txt)

# file=open(r"C:\Users\dorice asami\Desktop\intro_to_programming\week_2\quotes.txt","r")

# content=file.read()
# print(content)

#with statement

# with open(r"C:\Users\dorice asami\Desktop\intro_to_programming\week_2\quotes.txt","r") as file:
    
#     content = file.read()
    
#     print(content)

#readline content
# with open(r"C:\Users\dorice asami\Desktop\intro_to_programming\week_2\quotes.txt","r") as file:
    
#     content = file.readlines()

#     print(content[2])

 #append to a file

# with open(r"C:\Users\dorice asami\Desktop\intro_to_programming\week_2\quotes.txt","a") as file:
    
#     file.write("\nLife is for the living")

# with open(r"C:\Users\dorice asami\Desktop\intro_to_programming\week_2\quotes.txt","w") as file:
#     file.write("Hello world")



#encapsulating count function

def count(text,letter):
    "return number of times text appears in letter"

    return text.count(letter)
  
