a = 4
b = 5
while (a != b):
    if (a > b):
        a=a-b
    else:
        b=b-a
        print(a, b)

file = open("res.txt", "w")
file.write( str(a) + "   " +str(b))
file.close()