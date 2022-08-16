a="test web" #string
print(a)
b=20  #integer
print(b)
print(a.upper)  #output will be <built-in method upper of str object at 0x0000021B4A8F1DB0>
print(a.upper()) # TEST
print(a.lower())  # test
print(a. title()) # first letter of every word will be capital

print(len(a))  # length of the variable

c=2.33  # float
print(c)

# get integer part only
print(int(c))

#print("My name is "+a+" and I'm "+b+ " years old")  # TypeError: can only concatenate str (not "int") to str
print("My name is "+a+" and I'm "+str(b)+ " years old")

d=29
d+=1   # increment
print(d)  # 30