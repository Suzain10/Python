numbers = [10,1,2,13,1,4,16,78,90,55,67,24,48]
def even(x):
    return x % 2 == 0
evens = list(filter(even,numbers))
print("Even numbers: ",evens)

#Using Lambda Func:
numbers = [10,1,2,13,1,4,16,78,90,55,67,24,48]
even = list(filter(lambda x:x %2 ==0,numbers))
print(even)


city = ['Kota', 'Pune','Nasik','Mumbai','Chennai']
def length(city):
    return len(city)
sort = sorted(city,key=length)
print("Sorted words by length : ",sort)

city = ['Kota', 'Pune','Nasik','Mumbai','Chennai']
sort_1 = sorted((city, key= lambda x:len(x))
print("Sorted words by length : ",sort_1)