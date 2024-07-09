#string methods
text= 'pruthika is a good girl'
print (text.upper())
print (text.lower())
print (text.casefold())
print (text.capitalize())
print (text.title())

#strip method
a='      pruthika      '
print(a.strip())
print(a.lstrip())
print(a.rstrip())

#removing char
string ="abchello world."
string = string.lstrip("abc")
print(string)
string = string.rstrip("ld.")
print(string)

text='pruthika is a good girl'
print(text.startswith("pruthika"))
