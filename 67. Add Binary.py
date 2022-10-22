def addBinarey(a,b):
    return (str(bin(int(a,2)+int(b,2)))[2::])


a='11'
b='1'
a = "1010"
b = "1011"
print(addBinarey(a,b))