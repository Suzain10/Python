f = open('myfile.txt','r') 
i = 0
while True:
    i = i + 1
    line = f.readline()
    if not line:
     break
    m1 =line.split(",")[0]
    m2 =line.split(",")[1]
    m3 =line.split(",")[2]
    print(f"marks of student {i} in maths is:{m1}")
    print(f"marks of student {i} in science is:{m2}")
    print(f"marks of student {i} in english is:{m3}")
    print(line)


   

    