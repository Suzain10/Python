##Reading a file:

f = open('myfile.txt','r')
text = f.read()
print(text)
f.close()

##Writing to a file:
f = open('myfile2.txt', 'a')
f.write('It is March')
f.close()

with open('myfile2.txt','a') as f:
 f.write("Hey I am inside with")