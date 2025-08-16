#character classes
import re

# text='To call Police dial 199'
# pattern1=r'[A-Z]'
# print(re.findall(pattern1,text))

#search for matches 

# text='WiFi password is #tyhH0j8@22'

# password=re.findall(r'[A-Z]',text)

# print(password)

#escape character

# price='sugar costs $20'
# amount=re.findall('\$[0-9.]',price)

# print(amount)

# address='find us on wayuainvestments@yahoo.com'
# email=re.findall(r'[a-z@]',text)

# print(email)

# text='acd, a2d,abb bba'
# pattern='a..b'

# matches=re.findall(pattern,text)
# print(matches)

# text='cat scatter scattring category'
# pattern=r"\bcat\b"

# match=re.findall(pattern,text)
# print(match)

# text="regex is fun"
# pattern=r"\Bfun\b"

# match=re.findall(pattern,text)

# print=(match)

#find all words that start with py

# text="python is fun python programming"
# pattern=r"\bpy\w*\b"

# match=re.findall(pattern,text)

# print(match)

#find all words that have letters o or e within them

# text="hello world, i love python"

# pattern= r"\w*[oe]\w*"

# print =re.findall(pattern,text)

#pattern four digit numbers

# text= "year 2025 is number 1234"

# pattern = r"\d{4}"

# print=re.findall(pattern,text) 

# text="phone number is (254) 342-7865"

# pattern= r"(\(\d{3}\)),\s(\d{3}-\d{4})"

# match=re.search(pattern,text)

# print (match)
# #search
# print(match.group(0))
# print(match.group(1))
# print(match.group(2))

#find               
text = f"My email is dorice@example.com, or contact@domain.com"

pattern = r"\b[a-z]+@+[a-z]\.com\b" 

matches = re.findall(pattern,text)

print (matches)


